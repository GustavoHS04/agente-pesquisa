from config import get_modelo
from tools import data_atual, contar_palavras

tools = [data_atual, contar_palavras]
modelo = get_modelo().bind_tools(tools)

resposta = modelo.invoke(f"...")
print(resposta.text)
print(resposta.tool_calls)

por_nome = {t.name: t for t in tools}

for chamada in resposta.tool_calls:
    resultado = por_nome[chamada["name"]].invoke(chamada["args"])

    print(resultado)