"""
Gera uma sugestao de texto de decisao usando um LLM local (GGUF via
llama-cpp-python), alimentado com exemplos anteriores do seu proprio
estilo (config/exemplos_estilo.json).

Nenhum dado sai da maquina -- o modelo roda inteiramente offline apos
ser baixado uma vez.
"""
import json
from pathlib import Path

from llama_cpp import Llama

from extrator_base import Demanda

RAIZ = Path(__file__).parent.parent
MODELO_PATH = RAIZ / "modelos" / "modelo.gguf"
EXEMPLOS_PATH = RAIZ / "config" / "exemplos_estilo.json"

_llm = None


def _carregar_llm() -> Llama:
    global _llm
    if _llm is None:
        if not MODELO_PATH.exists():
            raise FileNotFoundError(
                f"Modelo nao encontrado em {MODELO_PATH}.\n"
                "Baixe um GGUF pequeno (ex: Qwen2.5-3B-Instruct-Q4_K_M.gguf) "
                "do Hugging Face e salve nesse caminho."
            )
        _llm = Llama(model_path=str(MODELO_PATH), n_ctx=4096, verbose=False)
    return _llm


def _carregar_exemplos() -> list:
    if EXEMPLOS_PATH.exists():
        return json.loads(EXEMPLOS_PATH.read_text(encoding="utf-8"))
    return []


def sugerir_texto(demanda: Demanda) -> str:
    llm = _carregar_llm()
    exemplos = _carregar_exemplos()[-5:]  # poucos exemplos mais recentes

    blocos_exemplo = "\n\n".join(
        f"Campos: {ex['campos']}\nTexto carimbado: {ex['texto']}" for ex in exemplos
    )

    prompt = (
        "Voce ajuda a redigir o texto de uma decisao de aprovacao corporativa.\n"
        "Use o mesmo estilo dos exemplos abaixo, seja objetivo e formal.\n\n"
        f"{blocos_exemplo}\n\n"
        f"Campos da nova demanda: {demanda.campos}\n"
        "Texto carimbado:"
    )

    resposta = llm(prompt, max_tokens=200, stop=["\n\n"])
    return resposta["choices"][0]["text"].strip()
