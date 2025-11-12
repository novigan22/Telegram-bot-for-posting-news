from google import genai
from dotenv import load_dotenv
import os


load_dotenv()
API_KEY = os.getenv('AI_API_KEY')
client = genai.Client(api_key=API_KEY)

def sum_text(text):
    response = client.models.generate_content(model="gemini-2.5-flash", 
                                              contents=('You must retell the following text without losing its meaning.' 
                                              'Loss of volume is possible, but it should not be critical.' 
                                              'Send only the retelling itself, without any remarks.'
                                              f'Here is the text to retell: {text}'))
    return response.text