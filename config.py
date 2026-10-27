from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv()

MODELO = "gpt-6-luna"
TEMPERATURA = 0


def get_modelo():
    return init_chat_model(
        MODELO,
        model_provider="openai",
    )