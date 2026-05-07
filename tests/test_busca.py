import time
from pages.home_page import HomePage

def test_busca_produto_aliexpress(driver):
    """
    Cenário de Teste: Buscar um produto no AliExpress lidando com popups.
    """
    termo_busca = "smartphone"
    
    # 1. Inicializa a Page Object da Home
    home_page = HomePage(driver)
    
    # 2. Acessa a URL da Home Page
    print("\nAcessando o AliExpress...")
    home_page.load()
    
    # 3. Tenta fechar possíveis popups que atrapalhem
    print("Verificando e fechando popups iniciais...")
    home_page.close_popups()
    
    # 4. Realiza a busca pelo produto
    print(f"Buscando por '{termo_busca}'...")
    home_page.search_for(termo_busca)
    
    # 5. Validação
    # Aguarda um momento para garantir que a página de resultados carregue e a URL mude
    time.sleep(3) 
    url_atual = driver.current_url
    
    print(f"URL de resultados: {url_atual}")
    # Verifica se a navegação foi para uma página de busca (AliExpress usa SearchText na query param)
    assert "SearchText" in url_atual or termo_busca in url_atual.lower(), f"Falha na navegação pós-busca. URL obtida: {url_atual}"
    print("Teste finalizado com sucesso!")
