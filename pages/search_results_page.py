from selenium.webdriver.common.by import By
from .base_page import BasePage

class SearchResultsPage(BasePage):
    # Locator para os títulos dos produtos na listagem
    # AliExpress usa div[role='heading'] para os títulos nos cards de produto
    PRODUCT_TITLES = (By.CSS_SELECTOR, "div[role='heading']")

    def __init__(self, driver):
        super().__init__(driver)

    def get_product_titles(self):
        """Retorna uma lista com o texto de todos os títulos de produtos visíveis."""
        elements = self.driver.find_elements(*self.PRODUCT_TITLES)
        return [el.text for el in elements if el.text.strip() != ""]

    def is_on_results_page(self, search_term):
        """Verifica se a URL atual condiz com uma página de resultados de busca."""
        url_atual = self.driver.current_url.lower()
        # AliExpress pode usar 'SearchText' ou 'wholesale-termo-com-hifens'
        term_slug = search_term.lower().replace(" ", "-")
        return "searchtext" in url_atual or term_slug in url_atual or "wholesale" in url_atual
