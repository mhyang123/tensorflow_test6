from urllib.request import urlopen
from bs4 import BeautifulSoup
from flask_restful import reqparse

class StockTickerController:
    def __init__(self,item):
        self._item=item
        self._code=''

    def service(self):
        parser = reqparse.RequestParser()
        parser.add_argument('tiker', type=str, required=True)
        args = parser.parse_args()
        print('입력된 URL : {}'.format(args.tiker))
        url='https://finance.naver.com/item/main.nhn?code='+'args.tiker'
        page = urlopen(url)
        soup = BeautifulSoup(page, 'html.parser')
        print(soup.prettify())
        price = soup.find('span', id = 'StockTicker_now')
        return price.string
