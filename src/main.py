"""
Fluxo completo: abre o navegador, extrai os campos da demanda, sugere
o texto via LLM local, deixa voce revisar/editar, preenche o campo no
sistema -- e o clique final de aprovar/reprovar fica sempre com voce.

Uso:
    python src/main.py --sistema exemplo --url https://sistema-x.empresa/demanda/123
"""
import argparse
import importlib

from playwright.sync_api import sync_playwright

from llm_sugestao import sugerir_texto
from log_decisoes import registrar
from revisao import revisar


def carregar_extrator(nome_sistema: str):
    modulo = importlib.import_module(f"extratores.{nome_sistema}")
    classe = next(
        v
        for k, v in vars(modulo).items()
        if k.lower().startswith("extrator") and k != "ExtratorBase"
    )
    return classe()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--sistema", required=True, help="nome do modulo em extratores/")
    parser.add_argument("--url", required=True, help="URL da demanda a revisar")
    args = parser.parse_args()

    extrator = carregar_extrator(args.sistema)

    with sync_playwright() as pw:
        navegador = pw.chromium.launch(headless=False)
        pagina = navegador.new_page()
        pagina.goto(args.url)

        input("Faca login / navegue até a tela da demanda e pressione Enter aqui...")

        demanda = extrator.extrair(pagina)
        texto_sugerido = sugerir_texto(demanda)
        texto_final = revisar(demanda, texto_sugerido)

        if texto_final is None:
            print("Cancelado -- nada foi preenchido.")
        else:
            extrator.preencher(pagina, texto_final)
            registrar(demanda, texto_sugerido, texto_final)
            print("Campo preenchido. Revise na tela e clique voce mesmo em aprovar/reprovar.")
            input("Pressione Enter para fechar o navegador...")

        navegador.close()


if __name__ == "__main__":
    main()
