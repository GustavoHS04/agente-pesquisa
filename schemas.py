from typing import Literal 
from pydantic import BaseModel, Field


class RespostaPesquisa(BaseModel):
    resposta: str = Field(
        description="Resposta direta à pergunta, em 2 a 4 frases, em língua portuguesa"
    )
    pontos_chave: list[str] = Field(
        description="De 3 a 5 pontos principais da resposta, cada um em uma frase curta"
    )
    confianca: Literal["alta", "média", "baixa"] = Field(
        description=(
            "Quão confiável é a resposta: "
            "'alta' para fatos amplamente conhecidos e consensuais, "
            "'média' quando há alguma incerteza ou o assunto é debatido, "
            "'baixa' quando você não tem certeza ou a informação pode estar desatualizada."
        )
    )

