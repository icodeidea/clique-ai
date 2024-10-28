from langchain_openai.chat_models import ChatOpenAI
from langchain_groq.chat_models import ChatGroq

openai_instance = ChatOpenAI(model="gpt-4o-mini")
groq_instance = ChatGroq(model="llama-3.1-70b-versatile")
llm = groq_instance
llm_instance = ChatGroq
