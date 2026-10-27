
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq

from app.core.config import settings


# Primary LLM
gemini = ChatGoogleGenerativeAI(
    model=settings.GEMINI_MODEL,
    google_api_key=settings.GEMINI_API_KEY,
    temperature=0,
    max_retries=1,
    timeout=20
)


# Fallback LLM 
groq = ChatGroq(
    model=settings.GROQ_MODEL,
    api_key=settings.GROQ_API_KEY,
    temperature=0,
    max_retries=1,
    timeout=20
)


# Use Gemini first, switch to Groq if Gemini fails
llm = gemini.with_fallbacks([groq])
