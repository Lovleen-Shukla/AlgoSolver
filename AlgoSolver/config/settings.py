import os 
from dotenv import load_dotenv
from config.constant import MODEL
from autogen_ext.models.openai import OpenAIChatCompletionClient

load_dotenv()
api_key=os.getenv('GEMINI_KEY')

def get_model_client():
    model_client=OpenAIChatCompletionClient(model=MODEL,api_key=api_key)
    return model_client