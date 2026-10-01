"""
Baixa o modelo GGUF padrao (Qwen2.5-3B-Instruct, ~2GB) direto do
Hugging Face para modelos/modelo.gguf. So precisa rodar uma vez.

Uso:
    python src/baixar_modelo.py
"""
from pathlib import Path

from huggingface_hub import hf_hub_download

REPO_ID = "Qwen/Qwen2.5-3B-Instruct-GGUF"
ARQUIVO = "qwen2.5-3b-instruct-q4_k_m.gguf"

DESTINO_DIR = Path(__file__).parent.parent / "modelos"
DESTINO_FINAL = DESTINO_DIR / "modelo.gguf"


def main():
    DESTINO_DIR.mkdir(exist_ok=True)
    print(f"Baixando {ARQUIVO} de {REPO_ID} (~2GB, so uma vez)...")
    caminho_baixado = hf_hub_download(
        repo_id=REPO_ID, filename=ARQUIVO, local_dir=DESTINO_DIR
    )
    Path(caminho_baixado).rename(DESTINO_FINAL)
    print(f"Pronto: {DESTINO_FINAL}")


if __name__ == "__main__":
    main()
