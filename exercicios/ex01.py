from selenium.webdriver import Chrome
from time import sleep

navegador  = Chrome()

URL = "https://curso-python-selenium.netlify.app/exercicio_01.html"
navegador.get(URL)

sleep(2) # Esperando o DOM carregar

h1_xpath = "/html/body/h1"
titulo = navegador.find_element("xpath", h1_xpath).text

p_xpath = "/html/body/p"
paragrafos = navegador.find_elements("xpath", p_xpath)

dicionario = {
    "h1": titulo,
    "p[1]": paragrafos[0].text,
    "p[2]": paragrafos[1].text,
    "p[3]": paragrafos[2].text,
} 


print(dicionario)