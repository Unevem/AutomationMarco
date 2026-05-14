import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from .base_page import BasePage

class HomePage(BasePage):
    URL = "https://pt.aliexpress.com/?gatewayAdapt=glo2bra"

    # Locators da barra de pesquisa
    SEARCH_INPUT = (By.ID, "search-words")
    # Alternativas caso o ID mude
    SEARCH_INPUT_ALT = (By.CSS_SELECTOR, "input[type='text'][placeholder*='Buscar']")
    
    # Locators de popups comuns (AliExpress usa classes ofuscadas, então tentamos estratégias mais amplas)
    COOKIES_ACCEPT = (By.XPATH, "//div[contains(@class, 'cookie')]//button | //button[contains(text(), 'Aceitar')]")
    POPUP_CLOSE_IMG = (By.CSS_SELECTOR, "img[src*='close'], img[src*='fechar']")
    POPUP_CLOSE_BTN = (By.CSS_SELECTOR, ".close-btn, .pop-close-btn, .ui-window-close")
    
    # Botão de pesquisa (lupa)
    SEARCH_BUTTON = (By.CLASS_NAME, "search--submit--2VTbd-T")
    
    # Lista de sugestões
    SUGGESTION_LIST = (By.CLASS_NAME, "search--optionList--19uL_I0")
    SUGGESTION_ITEMS = (By.CSS_SELECTOR, "li[id^='search-suggestions-']")

    def __init__(self, driver):
        super().__init__(driver)

    def load(self):
        """Acessa a página inicial do AliExpress."""
        self.open(self.URL)
        # Espera a página carregar um pouco para dar tempo de engatilhar os popups
        time.sleep(3)
        
    def close_popups(self):
        """Tenta encontrar e fechar modais/popups de ofertas e cookies."""
        
        # Tenta fechar o aviso de cookies
        if self.is_element_present(self.COOKIES_ACCEPT, timeout=3):
            try:
                self.click(self.COOKIES_ACCEPT)
                print("Cookies aceitos.")
            except Exception:
                pass

        # Tenta fechar popups baseados em botões ou imagens com 'close'
        for locator in [self.POPUP_CLOSE_IMG, self.POPUP_CLOSE_BTN]:
            if self.is_element_present(locator, timeout=2):
                try:
                    self.click(locator)
                    print(f"Popup fechado usando {locator}")
                    time.sleep(1) # Aguarda a animação de fechamento
                except Exception:
                    pass

    def search_for(self, text):
        """Realiza a busca de um produto pressionando ENTER."""
        # Tenta encontrar a barra de busca primária ou a alternativa
        input_locator = self.SEARCH_INPUT
        if not self.is_element_present(self.SEARCH_INPUT, timeout=3):
            input_locator = self.SEARCH_INPUT_ALT

        # Digita o texto e pressiona ENTER
        self.type_text(input_locator, text)
        element = self.find_element(input_locator)
        element.send_keys(Keys.RETURN)

    def search_with_button(self, text):
        """Realiza a busca digitando o texto e clicando no botão de lupa."""
        input_locator = self.SEARCH_INPUT
        if not self.is_element_present(self.SEARCH_INPUT, timeout=3):
            input_locator = self.SEARCH_INPUT_ALT

        self.type_text(input_locator, text)
        self.click(self.SEARCH_BUTTON)

    def get_suggestions(self, text):
        """Digita o texto e retorna a lista de sugestões que aparecem."""
        input_locator = self.SEARCH_INPUT
        if not self.is_element_present(self.SEARCH_INPUT, timeout=3):
            input_locator = self.SEARCH_INPUT_ALT

        # Digita sem apertar ENTER
        self.type_text(input_locator, text)
        
        # Espera um pouco para as sugestões carregarem
        time.sleep(2)
        
        if self.is_element_present(self.SUGGESTION_ITEMS, timeout=5):
            elements = self.driver.find_elements(*self.SUGGESTION_ITEMS)
            return [el.text for el in elements if el.text.strip() != ""]
        return []
