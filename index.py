import string
from bs4 import element
from selenium import webdriver
from selenium.webdriver.common.keys import Keys



#abrindo site
driver = webdriver.Chrome()
driver.get("https://www.bcb.gov.br/")
#extraindo informações
elemento =  driver.find_elements_by_tag_name('td')[1]
valorCompraDolar = str(elemento.text)
print('taxa de compra de câmbio calculada durante o dia foi ', valorCompraDolar)

elemento1 =  driver.find_elements_by_tag_name('td')[2]
valorVendaDolar = str(elemento1.text)
print('taxa de venda de câmbio calculada durante o dia foi ', valorVendaDolar)

elemeTd2 =  driver.find_elements_by_tag_name('td')[4]
valorCompraDolarInit = str(elemeTd2.text)
print('Valor inicial de compra',valorCompraDolarInit)

elemeTd20 =  driver.find_elements_by_tag_name('td')[5]
valorVendaDolarInit = str(elemeTd20.text)
print('Valor inicial de venda ',valorVendaDolarInit)
#verificando venda
valor = str('5,27')


if valor == valorVendaDolar[:4] or valor == valorVendaDolarInit[:4] :
   print('Compra efetuada!')

