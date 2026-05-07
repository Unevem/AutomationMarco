from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage:
    """
    Classe base que contém métodos genéricos do Selenium com Explicit Waits embutidos.
    Todas as outras Page Objects herdarão desta classe.
    """
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15) # Tempo máximo de espera padrão

    def open(self, url):
        """Abre uma URL no navegador"""
        self.driver.get(url)

    def find_element(self, locator):
        """Espera o elemento estar presente no DOM e o retorna"""
        return self.wait.until(EC.presence_of_element_located(locator))

    def click(self, locator):
        """Espera o elemento ser clicável e clica"""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def type_text(self, locator, text):
        """Espera o elemento estar visível, limpa e digita o texto"""
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def is_element_present(self, locator, timeout=5):
        """Verifica se um elemento está presente, útil para popups que podem ou não aparecer"""
        try:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
            return True
        except TimeoutException:
            return False
