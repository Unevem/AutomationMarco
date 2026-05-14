import pytest
import time
from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage

@pytest.fixture
def home_page(driver):
    hp = HomePage(driver)
    hp.load()
    hp.close_popups()
    return hp

def test_search_suggestions_visibility(home_page):
    """
    Caso de Teste 1: Testar se, ao digitar um nome de produto qualquer, 
    a barra retorna uma sugestão de itens.
    """
    termo = "iphone"
    print(f"\nTestando sugestões para: {termo}")
    sugestoes = home_page.get_suggestions(termo)
    
    print(f"Sugestões encontradas: {sugestoes}")
    assert len(sugestoes) > 0, "A lista de sugestões não apareceu ou está vazia."
    assert any(termo in s.lower() for s in sugestoes), f"Nenhuma sugestão contém o termo '{termo}'."

def test_search_with_enter(home_page, driver):
    """
    Caso de Teste 2: Testar se, ao digitar o nome completo de um produto e pressionar Enter, 
    a pesquisa retorna resultados condizentes.
    """
    termo = "fone de ouvido bluetooth"
    print(f"\nTestando busca com ENTER para: {termo}")
    home_page.search_for(termo)
    
    results_page = SearchResultsPage(driver)
    time.sleep(3) # Aguarda carregamento
    
    assert results_page.is_on_results_page(termo), f"Não navegou para a página de resultados de '{termo}'."
    titles = results_page.get_product_titles()
    assert len(titles) > 0, "Nenhum produto foi listado nos resultados."

def test_search_with_button(home_page, driver):
    """
    Caso de Teste 3: Testar se o botão de pesquisar item (lupa) realiza a mesma função do Enter.
    """
    termo = "teclado mecanico"
    print(f"\nTestando busca com BOTÃO para: {termo}")
    home_page.search_with_button(termo)
    
    results_page = SearchResultsPage(driver)
    time.sleep(3)
    
    assert results_page.is_on_results_page(termo), "O botão de busca não redirecionou para os resultados."
    titles = results_page.get_product_titles()
    assert len(titles) > 0, "Nenhum produto listado ao usar o botão de busca."

def test_search_results_content(home_page, driver):
    """
    Caso de Teste 4: Testar se os itens retornados possuem uma mesma descrição 
    fornecida pelo usuário (ou relacionada ao termo).
    """
    termo = "mouse gamer"
    print(f"\nTestando conteúdo dos resultados para: {termo}")
    home_page.search_for(termo)
    
    results_page = SearchResultsPage(driver)
    time.sleep(3)
    
    titles = results_page.get_product_titles()
    # Verifica os primeiros 5 títulos para garantir relevância
    relevantes = [t for t in titles[:5] if "mouse" in t.lower()]
    
    print(f"Títulos analisados: {titles[:5]}")
    assert len(relevantes) >= 3, f"Muitos resultados iniciais parecem irrelevantes para '{termo}'."
