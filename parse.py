import requests
import time
from random import uniform

def parse():
    full_names = []
    prices=[]
    inches = []
    CPUs = []
    SSDs = []
    urls = []

    cookies = {
        'ouid': 'snyBEGOORbWb6yXPbt34Ag==',
        '_gcl_au': '1.1.172808752.1670268344',
        '_ga_4Y6NQKE48G': 'GS1.1.1675096052.5.1.1675097521.13.0.0',
        '_ga': 'GA1.1.1130948357.1670268344',
        '_ga_NG54S9EFTD': 'GS1.1.1675096052.5.1.1675097521.0.0.0',
        '_tt_enable_cookie': '1',
        '_ttp': '393e82f4-b58c-4b60-bee7-5f887118ff4b',
        'tmr_lvid': '15b55881975ec4d6d380bdd0617e8c81',
        'tmr_lvidTS': '1637516314219',
        '_ym_uid': '1637516314610262777',
        '_ym_d': '1675093265',
        '_ym_isad': '1',
        '_gid': 'GA1.2.1077153917.1675093265',
        'catalog_session': 'rk2EIzI3GLfTEKHz2X21TpuzobVIv9GSTSnsgqkT',
        'delivery_boarding_showed': 'true',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'X-Requested-With': 'XMLHttpRequest',
        'Connection': 'keep-alive',
        'Referer': 'https://catalog.onliner.by/notebook?common_date^%^5Bfrom^%^5D=2022&common_date^%^5Bto^%^5D=2022',
        # 'Cookie': 'ouid=snyBEGOORbWb6yXPbt34Ag==; _gcl_au=1.1.172808752.1670268344; _ga_4Y6NQKE48G=GS1.1.1675096052.5.1.1675097521.13.0.0; _ga=GA1.1.1130948357.1670268344; _ga_NG54S9EFTD=GS1.1.1675096052.5.1.1675097521.0.0.0; _tt_enable_cookie=1; _ttp=393e82f4-b58c-4b60-bee7-5f887118ff4b; tmr_lvid=15b55881975ec4d6d380bdd0617e8c81; tmr_lvidTS=1637516314219; _ym_uid=1637516314610262777; _ym_d=1675093265; _ym_isad=1; _gid=GA1.2.1077153917.1675093265; catalog_session=rk2EIzI3GLfTEKHz2X21TpuzobVIv9GSTSnsgqkT; delivery_boarding_showed=true',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'If-None-Match': 'W/7871fd2b1cda0ba4ed80b99b6a3152cd',
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }

    for i in range(1,28):
        response = requests.get(
            f'https://catalog.onliner.by/sdapi/catalog.api/search/notebook?common_date[from]=2022&common_date[to]=2022&page={i}&page={i}',
            cookies=cookies,
            headers=headers,
        ).json()
        for j in dict(response)['products']:
            try:
                price = j['prices']['price_min']['amount']
            except:
                return (full_names,prices,inches,CPUs,SSDs,urls)
            else:
                descr = j['micro_description']
                full_names.append(j['full_name'])
                urls.append(j['html_url'])
                prices.append(price)
                descr = descr.replace('сенсорный,','')
                descr_list = descr.split(',')
                inches.append(descr_list[0])
                CPUs.append(descr_list[1])
                SSDs.append(descr_list[3])
        time.sleep(uniform(0.5,1.5))