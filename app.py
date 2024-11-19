import os
import dotenv
from fastapi import FastAPI
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langserve import add_routes

dotenv.load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")

model = ChatGroq(model = "Gemma2-9b-It", groq_api_key = groq_api_key)

parser = StrOutputParser()

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful and knowledgeable healthcare assistant. You provide information and support for health-related concerns. You offer insights, suggestions, and potential considerations, empowering users to make informed decisions about their well-being. Emphasize the importance of seeking guidance from qualified healthcare professionals for personalized advice and treatment."),
    ("user", "{user_input}")
])


# combine all together and create chain
chain = prompt | model | parser


## app defenition
app = FastAPI(title='Healthcare chatbot  Server',
              version='1.0',
              description='A simple API server using Langchain runnable interfaces')

# adding chain routes 
add_routes(
    app,
    chain,
    path="/chain"
)


if __name__== '__main__':
    import uvicorn
    uvicorn.run(app)