import requests

class Markit:
    def __init__(self):
        self.lookup_url = "http://dev.markitondemand.com/Api/v2/Lookup/json?input="
        self.quote_url = "http://dev.markitondemand.com/Api/v2/Quote/json?symbol="

def get_company_sym(string):
    url_concat = "http://dev.markitondemand.com/Api/v2/Lookup/json?input=" + string
    r = requests.get(url_concat)
    data = r.json()
    if r.status_code == 200:
        if len(data) == 0:
            return False
        else:
            symbol = data[0]['Symbol']
            return  symbol
    else:
        return False


def get_stock_price(string):
    none = 0.0
    if string is not None:
        url_concat = "http://dev.markitondemand.com/Api/v2/Quote/json?symbol=" + string
        r = requests.get(url_concat)
        if r.status_code == 200:
            data = r.json()
            name = None
            price = None
            if len(data) > 0:
                for key in data:
                    if key == 'LastPrice':
                        price = (data[key])
                    if key == 'Name':
                        name = data[key]
            return [name, price]
        else:
            print('\n\n\n')
            print('API STATUS CODE:' + str(r.status_code))
            print('\n\n\n')
            return [None, none]
    else:
        return [None, none]


def get_stock_change(string):
    none = 0.0
    if string is not None:
        url_concat = "http://dev.markitondemand.com/Api/v2/Quote/json?symbol=" + string
        r = requests.get(url_concat)
        if r.status_code == 200:
            data = r.json()
            price = None
            per_ch = None
            today_ch = None
            if len(data) > 0:
                for key in data:
                    if key == 'LastPrice':
                        price = (data[key])
                    if key == 'Change':
                        today_ch = (data[key])
                    if key == 'ChangePercent':
                        per_ch = data[key]
            return [price, today_ch,per_ch]
        else:
            print('\n\n\n')
            print('API STATUS CODE:' + str(r.status_code))
            print('\n\n\n')
            return [none, none, none]
    else:
        return [none, none, none]

def get_stock_details(string):
    none = 0.0
    name=""
    if string is not None:
        url_concat = "http://dev.markitondemand.com/Api/v2/Quote/json?symbol=" + string
        r = requests.get(url_concat)
        if r.status_code == 200:
            data = r.json()
            price = None
            change =None
            per_change = None
            high = None
            low = None
            if len(data) > 0:
                for key in data:
                    if key == 'LastPrice':
                        price = (data[key])
                    if key == 'Name':
                        name = data[key]
                    if key == 'Change':
                        change = (data[key])
                    if key == 'ChangePercent':
                        per_change = data[key]
                    if key == 'High':
                        high = (data[key])
                    if key == 'Low':
                        low = data[key]                    
            return [name, price, change, per_change, high, low]
        else:
            print('\n\n\n')
            print('API STATUS CODE:' + str(r.status_code))
            print('\n\n\n')
            return [name, none, none, none, none, none]
    else:
        return [name, none, none, none, none, none]






if __name__ == "__main__":
    # get company info test
    # print(get_company_info('apple'))
    session.commit()
    # # get stock price test - returns name and price
    # print(get_stock_price('aapl'))
