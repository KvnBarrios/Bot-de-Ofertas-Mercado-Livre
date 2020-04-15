import xlsxwriter
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from utils.support import wait_for_element

workbook = xlsxwriter.Workbook('ofertas.xlsx')
worksheet = workbook.add_worksheet('Ofertas do MercadoLivre')
row = row1 = row2 = row3 = row4 = 0

worksheet.write(0, 0, 'Produtos')
worksheet.write(0, 1, 'Preço')
worksheet.write(0, 2, 'Preço anterior')
worksheet.write(0, 3, 'Desconto')
worksheet.write(0, 4, 'Link')

driver: WebDriver = webdriver.Chrome()
driver.get("https://www.mercadolivre.com.br/ofertas")

pages = int(
    driver.find_element_by_xpath('/html/body/main/div/div[2]/div[2]/div/ul/li[12]/a').get_attribute('innerHTML'))

for page in range(pages):
    for names in driver.find_elements_by_class_name('promotion-item__title'):
        worksheet.write(row + 1, 0, names.get_attribute('innerHTML'))
        row += 1

    for price in driver.find_elements_by_class_name('promotion-item__price'):
        real = price.find_element_by_tag_name('span')
        try:
            cents = price.find_element_by_tag_name('sup')
            worksheet.write(row1 + 1, 1, real.text + ',' + cents.text)
        except NoSuchElementException:
            worksheet.write(row1 + 1, 1, real.text)
        row1 += 1

    for old_price in driver.find_elements_by_class_name('promotion-item__oldprice'):
        worksheet.write(row2 + 1, 2, old_price.text)
        row2 += 1

    for discount in driver.find_elements_by_class_name('promotion-item__discount'):
        worksheet.write(row3 + 1, 3, discount.text)
        row3 += 1

    for link in driver.find_elements_by_class_name('promotion-item__link-container'):
        worksheet.write(row4 + 1, 4, link.get_attribute('href'))
        row4 += 1

    driver.get(f'https://www.mercadolivre.com.br/ofertas?page={page + 2}')
    wait_for_element(driver, (By.CLASS_NAME, 'promotion-item__title'))

workbook.close()
