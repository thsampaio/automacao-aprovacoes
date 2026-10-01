"""
Mostra a demanda + texto sugerido e deixa o humano decidir -- aceitar,
editar ou cancelar. O clique final de aprovar/reprovar no sistema fica
sempre com voce, nunca automatizado.
"""
from typing import Optional

from extrator_base import Demanda


def revisar(demanda: Demanda, texto_sugerido: str) -> Optional[str]:
    print("\n" + "=" * 60)
    print(f"Sistema: {demanda.sistema}")
    print(f"Campos: {demanda.campos}")
    print("-" * 60)
    print(f"Texto sugerido:\n{texto_sugerido}")
    print("-" * 60)
    resposta = input(
        "Enter = aceitar | digite um novo texto = editar | 'c' = cancelar: "
    ).strip()

    if resposta.lower() == "c":
        return None
    if resposta == "":
        return texto_sugerido
    return resposta
