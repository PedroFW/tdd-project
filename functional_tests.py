from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import unittest

class NewVisitorTest(unittest.TestCase):

    def test_can_start_a_list_and_retrieve_it_later(self): 
    
        options = Options()
        options.add_argument("-profile")
        options.add_argument("/home/pedro/snap/firefox/common/.mozilla/firefox/va7i427w.pedro")
        browser=webdriver.Firefox(options=options)

        browser.get('http://localhost:8000')

        # Ela nota que o título da página menciona TODO
        assert 'To-Do' in browser.title

        # Ela é convidada a entrar com um item TODO imediatamente

        # Ela digita "Estudar testes funcionais" em uma caixa de texto

        # Quando ela aperta enter, a página atualiza, e mostra a lista
        # "1: Estudar testes funcionais" como um item da lista TODO
        
        # Ainda existe uma caixa de texto convidando para adicionar outro item
        # Ela digita: "Estudar testes de unidade"

        # A página atualiza novamente, e agora mostra ambos os itens na sua lista

        # Maria se pergunta se o site vai lembrar da sua lista. Então, ela verifica que
        # o site gerou uma URL única para ela -- existe uma explicação sobre essa feature

        # Ela visita a URL: a sua lista TODO ainda está armazenada

        # Satisfeita, ela vai dormir
        
        self.browser.quit()

if __name__ == '__main__':
    unittest.main()

