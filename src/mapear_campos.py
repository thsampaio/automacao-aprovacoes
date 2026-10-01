"""
Grava os seletores de uma tela de aprovacao usando o Playwright Codegen.

Uso:
    python src/mapear_campos.py <url_do_sistema>

Abre um navegador. Navegue manualmente até a tela de aprovacao real e
clique/selecione os campos que te interessam (solicitante, valor,
justificativa, etc). O Codegen grava o codigo Python com os seletores
correspondentes na janela ao lado -- copie o que precisar para um novo
arquivo em extratores/sistema_x.py (veja extratores/exemplo.py).
"""
import subprocess
import sys


def main():
    if len(sys.argv) < 2:
        print("Uso: python mapear_campos.py <url>")
        sys.exit(1)
    url = sys.argv[1]
    subprocess.run(["playwright", "codegen", url])


if __name__ == "__main__":
    main()
