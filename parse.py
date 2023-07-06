import pathlib
from bs4 import BeautifulSoup as BS


def get_soup(html:str) -> BS:
    return BS(html, 'lxml')


def get_page_data(soup:BS):
    location = soup.find('h1', class_='CurrentConditions--location--1YWj_').text
    degree = soup.find('span', class_='CurrentConditions--tempValue--MHmYY').text
    condition = soup.find('div', class_='CurrentConditions--phraseValue--mZC_p').text
    
    data = {
        'location': location,
        'degree': degree,
        'condition': condition
    }
    
    write_to_db(data)


def write_to_db(data):
    import json
    with open('forecast.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


# def main():
#     forecast = pathlib.Path('forecast.html').read_text()
#     get_page_data(get_soup(forecast))


# if __name__ == '__main__':
#     main()

    