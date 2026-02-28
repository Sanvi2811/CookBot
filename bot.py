import os
from dotenv import load_dotenv
import google.generativeai as genai


load_dotenv()

def generate():
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
"""
        )

       
        chat = model.start_chat(history=[])

        print("Bot: Hello, which taste meal would we make today?")

        while True:
            user_input = input("You: ")
            if user_input.lower() in ['exit', 'quit']:
                print("Bot: See you soon!")
                break

            try:
                response = chat.send_message(user_input)
                print(f"Bot: {response.text}\n")
            except Exception as e:
                print(f"Error generating response: {e}")
                print("Bot: Sorry, I encountered an error. Please try again.\n")

    except Exception as e:
        print(f"Error initializing the bot: {e}")
        print("Please check your API key and internet connection.")

def generate_bot_response(user_input):
    try:
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

        model = genai.GenerativeModel(
            model_name="gemini-2.5-flash",
            system_instruction="""
You are Cookbot, a super friendly, cheerful, and knowledgeable Indian cuisine expert. You act as a digital Indian cookbook and kitchen companion.
"""
        )

        chat = model.start_chat(history=[])
        response = chat.send_message(user_input)
        return response.text

    except Exception as e:
        return "Sorry, something went wrong while generating the response."



if __name__ == "__main__":
    generate()
