from baseparser import BaseParser
from time import time
from product_page import Additional


class CreditAsiaParser(BaseParser, Additional):
    def __init__(self):
        super(CreditAsiaParser, self).__init__()

    def get_data(self):
        soup = self.get_soup(self.get_html())
        form_filter = soup.find('div', class_='form-filter')
        categories = form_filter.find_all('li')
        for category in categories[:3]:
            category_title = category.get_text(strip=True)
            print(category_title)
            category_link = self.HOST + category.find('a').get('href')
            print(category_link)
            self.products_page_parsing(category_title, category_link)

    def products_page_parsing(self, category_title, category_link):
        soup = self.get_soup(self.get_html(category_link))
        flex_catalog = soup.find('div', class_='flex-catalog')
        products = flex_catalog.find_all('div', class_='product_slider-card')
        for product in products[:3]:
            product_title = product.find('a', class_='product_slider-name').get_text(strip=True)
            print(product_title)
            product_link = self.HOST + product.find('a', class_='product_slider-name').get('href')
            print(product_link)
            try:
                product_price = product.find('div', class_='price').get_text(strip=True)
                product_price = int(product_price.replace(' ', '').replace('сум', ''))
            except:
                product_price = 0
            print(product_price)
            product_image = self.HOST + product.find('img').get('data-lazy')
            print(product_image)
            try:
                data = self.get_product_data(link=product_link)
                desc = data[1]
                characteristics = data[0]
                print(desc)
                print(characteristics)
            except:
                print('На сайте характеристики не указаны')


        # Сделать переход на детали товара. Сохранить подробные характеристики
        # Сделать сохранение категорий и товаров в базу данных


def start_parsing():
    start = time()
    parser = CreditAsiaParser()
    parser.get_data()
    finish = time()
    print(f'Парсер отработал за {finish - start} секунд')

start_parsing()



