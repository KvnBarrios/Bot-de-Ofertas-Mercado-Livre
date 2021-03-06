import xlsxwriter
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from utils.support import wait_for_element
from selenium.webdriver.chrome.options import Options
from art import *
from datetime import date

byebye = text2art("KvnBarrios")

workbook = xlsxwriter.Workbook(f'ofertas_dia_{date.today()}.xlsx')
worksheet = workbook.add_worksheet('Ofertas do MercadoLivre')
row = row1 = row2 = row3 = row4 = 1

worksheet.write(0, 0, 'Produtos')
worksheet.write(0, 1, 'Preço')
worksheet.write(0, 2, 'Preço anterior')
worksheet.write(0, 3, 'Desconto')
worksheet.write(0, 4, 'Link')

chrome_options = Options()
chrome_options.add_argument("--headless")
driver: WebDriver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.mercadolivre.com.br/ofertas")

pages = int(
    driver.find_element_by_xpath('/html/body/main/div/div[2]/div[2]/div/ul/li[12]/a').get_attribute('innerHTML'))

print(f'Estamos na pagina 1 de um total de {pages}')

for page in range(pages):
    for names in driver.find_elements_by_class_name('promotion-item__title'):
        worksheet.write(row, 0, names.get_attribute('innerHTML'))
        row += 1

    for price in driver.find_elements_by_class_name('promotion-item__price'):
        real = price.find_element_by_tag_name('span')
        try:
            cents = price.find_element_by_tag_name('sup')
            worksheet.write(row1, 1, real.text + ',' + cents.text)
        except NoSuchElementException:
            worksheet.write(row1, 1, real.text)
        row1 += 1

    for old_price in driver.find_elements_by_class_name('promotion-item__oldprice'):
        worksheet.write(row2, 2, old_price.text)
        row2 += 1

    for discount in driver.find_elements_by_class_name('promotion-item__discount'):
        worksheet.write(row3, 3, discount.text[0:3])
        row3 += 1

    for link in driver.find_elements_by_class_name('promotion-item__link-container'):
        worksheet.write_url(row4, 4, link.get_attribute('href'), string='Link')
        row4 += 1

    driver.get(f'https://www.mercadolivre.com.br/ofertas?page={page + 2}')
    if page + 2 <= pages:
        print(f'Estamos na pagina {page + 2} de um total de {pages}')
        wait_for_element(driver, (By.CLASS_NAME, 'promotion-item__title'))
    else:
        print('O Bot terminou :)')
        print(byebye)

workbook.close()
