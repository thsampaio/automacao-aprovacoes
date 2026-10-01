"""
Log local das decisoes (CSV) -- serve de trilha de auditoria e tambem
de base de exemplos para o LLM manter seu estilo com o tempo.
Fica em historico/, que e ignorado pelo git (nunca sobe pro GitHub).
"""
import csv
import json
from datetime import datetime
from pathlib import Path

from extrator_base import Demanda

LOG_PATH = Path(__file__).parent.parent / "historico" / "decisoes.csv"


def registrar(demanda: Demanda, texto_sugerido: str, texto_final: str) -> None:
    LOG_PATH.parent.mkdir(exist_ok=True)
    novo = not LOG_PATH.exists()
    with LOG_PATH.open("a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if novo:
            writer.writerow(
                ["timestamp", "sistema", "campos", "texto_sugerido", "texto_final"]
            )
        writer.writerow(
            [
                datetime.now().isoformat(),
                demanda.sistema,
                json.dumps(demanda.campos, ensure_ascii=False),
                texto_sugerido,
                texto_final,
            ]
        )
