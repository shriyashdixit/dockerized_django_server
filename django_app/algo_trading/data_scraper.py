import requests
from .models import LiveDataNSE
from datetime import datetime


class NSE:
    def __init__(self):
        self.baseurl = "https://www.nseindia.com/"
        self.url = r'https://www.nseindia.com/api/quote-equity?symbol='
        self.headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, '
                        'like Gecko) '
                        'Chrome/80.0.3987.149 Safari/537.36',
                        'accept-language': 'en,gu;q=0.9,hi;q=0.8', 'accept-encoding': 'gzip, deflate, br'}

    def live_data(self):
        session = requests.Session()
        request = session.get(self.baseurl, headers=self.headers, timeout=5)
        cookies = dict(request.cookies)
        ticker = ['RELIANCE', 'SBIN', 'AXISBANK', 'TATAPOWER', 'TCS', 'INFY', 'WIPRO', 'LUPIN', 'BPCL']
        for symbol in ticker:
            try:
                res = session.get(self.url + symbol, headers=self.headers, timeout=5, cookies=cookies)
                all_data = res.json()['priceInfo']['lastPrice']
                LiveDataNSE.objects.create(
                    ticker=symbol,
                    date=datetime.now(),
                    price=all_data)
            except Exception as e:
                print(e)
                pass
        session.close()
