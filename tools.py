from langchain.tools import tool

@tool
def data_atual() -> str:
    """Retorna a data atual no formato DD/MM/YYYY"""
    from datetime import date

    return date.today().strftime("%d/%m/%Y")

@tool
def contar_palavras(texto: str) -> int:
    """Conta e retorna o número de palavras presentes em um texto"""
    import re

    palavras = re.findall(r'\b\w+\b', texto)

    return len(palavras)