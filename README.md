# Automação de Testes - AliExpress

Este projeto contém uma suite de testes automatizados para a funcionalidade de busca do site AliExpress, utilizando Python, Selenium e Pytest.

## 🚀 Tecnologias Utilizadas

*   **Linguagem:** Python 3.x
*   **Framework de Teste:** Pytest
*   **Automação Web:** Selenium WebDriver
*   **Padrão de Projeto:** Page Object Model (POM)

## 📁 Estrutura do Projeto

*   `pages/`: Contém as Page Objects, que mapeiam os elementos e ações de cada página.
    *   `base_page.py`: Métodos genéricos e esperas explícitas.
    *   `home_page.py`: Elementos da página inicial e lógica de busca/popups.
    *   `search_results_page.py`: Elementos e validações da página de resultados.
*   `tests/`: Contém os scripts de teste.
    *   `test_search_scenarios.py`: Cenários principais baseados no plano de teste.
    *   `test_busca.py`: Teste inicial de fumaça.
*   `conftest.py`: Configuração de fixtures do Pytest (ex: inicialização do browser).
*   `requirements.txt`: Lista de dependências do projeto.

## 🛠️ Instalação

1.  Certifique-se de ter o Python instalado.
2.  Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

## 🧪 Como Executar os Testes

Para rodar todos os testes com detalhes no console:
```bash
python -m pytest -s -v
```

Para rodar apenas a suite principal de cenários:
```bash
python -m pytest tests/test_search_scenarios.py -s -v
```

## 📝 Cenários Cobertos

A suite `test_search_scenarios.py` cobre os seguintes pontos do plano de teste:

1.  **Sugestões de Busca**: Valida se a lista de sugestões aparece ao digitar um termo.
2.  **Busca com Enter**: Valida se a pesquisa funciona corretamente ao pressionar a tecla Enter.
3.  **Botão de Pesquisa**: Valida se clicar na lupa de pesquisa realiza a navegação correta.
4.  **Relevância dos Resultados**: Valida se os primeiros itens retornados possuem o termo pesquisado no título.

## 💡 Observações
*   O projeto possui uma lógica de fechamento automático de popups e aceitação de cookies para evitar interrupções nos testes.
*   Utiliza esperas explícitas (`Explicit Waits`) para garantir a estabilidade em ambientes com oscilação de rede.
