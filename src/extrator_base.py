from dataclasses import dataclass, field
from playwright.sync_api import Page


@dataclass
class Demanda:
    sistema: str
    campos: dict = field(default_factory=dict)


class ExtratorBase:
    """Extrai os campos de uma demanda de uma tela de aprovacao.

    Cada sistema tem sua propria subclasse em extratores/, com os
    seletores gravados via `python src/mapear_campos.py <url>`.
    """

    nome_sistema = "generico"

    def extrair(self, page: Page) -> Demanda:
        raise NotImplementedError(
            "Implemente extrair() usando os seletores gravados com mapear_campos.py"
        )

    def preencher(self, page: Page, texto: str) -> None:
        """Preenche o campo de texto da decisao com o texto final revisado.
        O clique final de aprovar/reprovar continua manual, por voce."""
        raise NotImplementedError(
            "Implemente preencher() com o seletor do campo de texto da decisao"
        )
