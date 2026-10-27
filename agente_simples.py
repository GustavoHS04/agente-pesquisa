from langchain.agents import create_agent

from config import get_modelo
from tools import data_atual, contar_palavras

agente = create_agent(
    get_modelo(),
    tools=[data_atual, contar_palavras],
    system_prompt="""\
        Você é um agente de pesquisa, responda com frases curtas e simples,
        seja totalmente honesto em suas respostas e, quando não souber
        diga apenas que não sabe. Utilize as tools fornecidas para auxiliar
        nas respostas quando necessário.\
    """,
)

resultado = agente.invoke(
    {"messages": [{"role": "user", "content": "Qual é o dia de hoje? Que dia foi ontem?"}]}
)

for mensagem in resultado["messages"]:
    mensagem.pretty_print()

print(resultado["messages"][-1].text)