"""
Modelo de extrator. Copie este arquivo para cada sistema real
(ex: sistema_x.py) e troque os seletores pelos gravados com
mapear_campos.py.
"""
from playwright.sync_api import Page

from extrator_base import Demanda, ExtratorBase


class ExtratorExemplo(ExtratorBase):
    nome_sistema = "exemplo"

    def extrair(self, page: Page) -> Demanda:
        campos = {
            "solicitante": page.locator("#TODO_seletor_solicitante").inner_text(),
            "valor": page.locator("#TODO_seletor_valor").inner_text(),
            "justificativa": page.locator("#TODO_seletor_justificativa").inner_text(),
        }
        return Demanda(sistema=self.nome_sistema, campos=campos)

    def preencher(self, page: Page, texto: str) -> None:
        page.locator("#TODO_seletor_campo_decisao").fill(texto)
