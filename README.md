# Automacao de Aprovacoes

Copiloto local para triagem de aprovacoes em sistemas web internos:
extrai os campos da demanda, sugere o texto da decisao (LLM 100% local,
nenhum dado sai da maquina) e deixa voce revisar/editar antes de
preencher. **O clique final de aprovar/reprovar continua sempre manual.**

## Setup (uma vez)

```bash
pip install -r requirements.txt
playwright install chromium
```

Baixe o modelo (Qwen2.5-3B-Instruct, ~2GB, bom suporte a portugues):

```bash
python src/baixar_modelo.py
```

A partir dai a inferencia roda 100% offline.

## Mapear um sistema novo

1. Grave os seletores da tela de aprovacao:

   ```bash
   python src/mapear_campos.py https://sistema-x.empresa/alguma-demanda
   ```

   Navegue manualmente até a tela real. O Codegen mostra o codigo
   com os seletores dos campos que voce clicar/selecionar.

2. Copie `src/extratores/exemplo.py` para `src/extratores/sistema_x.py`
   e troque os seletores `#TODO_...` pelos que o Codegen gravou --
   tanto para os campos a extrair (`extrair`) quanto para o campo onde
   o texto final sera preenchido (`preencher`).

## Uso diario

```bash
python src/main.py --sistema sistema_x --url https://sistema-x.empresa/demanda/123
```

O navegador abre, voce faz login/navega até a demanda, aperta Enter
no terminal. O script extrai os campos, sugere o texto, mostra pra
voce revisar (aceitar / editar / cancelar), preenche o campo -- e voce
mesmo confirma a aprovacao na tela.

## Estilo de carimbo

`config/exemplos_estilo.json` guarda exemplos de decisoes anteriores
para o LLM manter seu estilo. Formato:

```json
[
  {
    "campos": {"solicitante": "...", "valor": "...", "justificativa": "..."},
    "texto": "Texto da decisao que voce escreveu nesse caso"
  }
]
```

Vai crescendo sozinho: `historico/decisoes.csv` guarda cada decisao
registrada e pode alimentar esse arquivo com o tempo.

## Privacidade

`modelos/` e `historico/` estao no `.gitignore` -- nenhum dado real ou
peso de modelo sobe para o repositorio, mesmo sendo privado.
