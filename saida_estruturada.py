from langchain_core.prompts import ChatPromptTemplate

from config import get_modelo
from schemas import RespostaPesquisa


prompt = ChatPromptTemplate.from_messages([
    ("system", "Você é um assistente de pesquisa. Responda de forma objetiva "
                "e honesta. Se não souber responder, diga que não sabe."),
    ("human", "{pergunta}"),
])


modelo = get_modelo().with_structured_output(RespostaPesquisa)

cadeia = prompt | modelo

resultado = cadeia.invoke({"pergunta": "Qual o seu nome?"})

print(resultado.resposta)
print(resultado.pontos_chave)
print(resultado.confianca)