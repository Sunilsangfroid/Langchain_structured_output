import os
from langchain_google_genai import ChatGoogleGenerativeAI
from typing import TypedDict
from dotenv import load_dotenv

load_dotenv()

google_api_key = os.getenv("GOOGLE_API_KEY")
if not google_api_key:
    raise ValueError("GOOGLE_API_KEY is not set in the environment variables")

model = ChatGoogleGenerativeAI(model='gemini-1.5-pro', api_key=google_api_key)

# Schema
class Review(TypedDict):
    summary: str
    sentiment: str
    
structured_model = model.with_structured_output(Review)
print(structured_model)
result = structured_model.invoke("""The hardware is great, but the software feels bloated. There are too many pre-installed apps that i can't remove. Also, the UI looks outdated compared to other brands. Hoping for a software update to fix this """)

print(result)