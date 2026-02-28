from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()


app = Flask(__name__)
CORS(app) 


try:
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    

    model = genai.GenerativeModel(
        model_name="gemini-2.5-flash",  
        system_instruction="""
You are Cookbot, a super friendly, cheerful, and knowledgeable Indian cuisine expert. You act as a digital Indian cookbook and kitchen companion.

Your primary responsibilities include:
- Recipe Expert: Provide step-by-step recipes for all Indian cuisines — North, South, Gujarati, Maharashtrian, Bengali, Jain, etc.
- Meal Planner: Suggest ideal food combinations.
- Leftover Advisor: Suggest recipes using leftover ingredients.
- Customization: Offer no onion-garlic, Jain, or healthier versions when requested.
- Fun Facts: Occasionally share cultural or historical background about dishes.

Use clear, friendly language. You're a kitchen companion — supportive, knowledgeable, and approachable.
Always respond in a conversational, helpful manner. Keep responses concise but informative.
"""
    )
    

    chat_session = None
    
except Exception as e:
    print(f"Error initializing Gemini AI: {e}")
    model = None


@app.route('/')
def index():
    """Serve the welcome page"""
    return render_template('frontend.html')

@app.route('/chat')
def chat_page():
    """Serve the chat page"""
    return render_template('page_2.html')

@app.route('/api/chat', methods=['POST'])
def chat_api():
    """Handle chat messages from the frontend"""
    global chat_session
    
    try:
        data = request.get_json()
        user_message = data.get('message', '').strip()
        
        if not user_message:
            return jsonify({'error': 'Message cannot be empty'}), 400
        
        if not model:
            return jsonify({'error': 'AI model not initialized. Please check your API key.'}), 500
        
       
        if chat_session is None:
            chat_session = model.start_chat(history=[])
        
       
        response = chat_session.send_message(user_message)
        bot_response = response.text
        
        return jsonify({
            'response': bot_response,
            'status': 'success'
        })
        
    except Exception as e:
        import traceback
        print(f"Error in chat API: {e}")
        traceback.print_exc()
        return jsonify({
            'error': 'Sorry, I encountered an error while processing your request. Please try again.',
            'status': 'error'
        }), 500

@app.route('/api/new-chat', methods=['POST'])
def new_chat():
    """Start a new chat session"""
    global chat_session
    
    try:
        if model:
            chat_session = model.start_chat(history=[])
            return jsonify({
                'message': 'New chat started successfully!',
                'status': 'success'
            })
        else:
            return jsonify({'error': 'AI model not initialized'}), 500
            
    except Exception as e:
        print(f"Error starting new chat: {e}")
        return jsonify({'error': 'Failed to start new chat'}), 500

@app.route('/api/health')
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'model_initialized': model is not None,
        'api_key_configured': bool(os.getenv("GEMINI_API_KEY"))
    })


@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Endpoint not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    
    if not os.getenv("GEMINI_API_KEY"):
        print("WARNING: GEMINI_API_KEY not found in environment variables!")
        print("Please create a .env file with your Gemini API key:")
        print("GEMINI_API_KEY=your_api_key_here")
    else:
        print("Gemini API key configured")
    
    print("Starting Cook Bot Flask Application...")
    print("Welcome page: http://localhost:5000")
    print("Chat page: http://localhost:5000/chat")
    
  
    app.run(debug=True, host='0.0.0.0', port=5000)