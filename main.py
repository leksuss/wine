import argparse
from datetime import date
from http.server import HTTPServer, SimpleHTTPRequestHandler

import pandas
from jinja2 import Environment, FileSystemLoader, select_autoescape


SINCE_YEAR = 1920


def read_args():
    parser = argparse.ArgumentParser(
        description='''
            Runs server for wine website store.
            Data for website gets from xlsx file.
        '''
    )
    parser.add_argument('filepath', help='path to xlsx file with wine data')
    args = parser.parse_args()
    return args


def get_declension_year(num):
    if num % 100 in range(11, 15):
        return 'лет'
    if num % 10 in range(2, 5):
        return 'года'
    if num % 10 == 1:
        return 'год'
    return 'лет'


def read_excel(filepath):
    excel_df = pandas.read_excel(
        filepath,
        sheet_name='Лист1',
        na_values=None,
        keep_default_na=False,
    )

    return excel_df.to_dict('records')


def group_categories(wines):
    wine_categories = {}
    for wine in wines:
        wine_categories.setdefault(wine.pop('Категория'), []).append(wine)
    return wine_categories


def prepare_page(wines):
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('template.html')

    passed_years = date.today().year - SINCE_YEAR

    rendered_page = template.render(
        year_with_us=f'{passed_years} {get_declension_year(passed_years)}',
        wine_categories=group_categories(wines),
    )

    return rendered_page


def runserver(rendered_page):
    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == '__main__':

    filepath = read_args().filepath

    rendered_page = prepare_page(read_excel(filepath))

    runserver(rendered_page)
