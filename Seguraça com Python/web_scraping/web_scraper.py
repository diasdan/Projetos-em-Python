from bs4 import BeautifulSoup
import requests

site = requests.get("https://www.climatempo.com.br/").content
# objeto site -> recebe todo o conteúdo da requisição http do site
soup = BeautifulSoup(site, 'html.parser')
# objeto soup -> baixa o html do site
print(soup.prettify())
# prettify converte o codigo para string para ser imprimível

titulo = soup.find("title") #busca a tag title e armazena na variavel titulo
print(titulo.string) #printa o conteudo da tag no formato string

print(soup.p) #acha a primeira tag p do site