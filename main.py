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
    parser.add_argument('filename', help='xlsx file with wine data')
    args = parser.parse_args()
    return args


def declension_year(num):
    if num % 100 in range(11, 15):
        return 'лет'
    if num % 10 in range(2, 5):
        return 'года'
    if num % 10 == 1:
        return 'год'
    return 'лет'


def read_excel(filename):
    excel_data_df = pandas.read_excel(
        filename,
        sheet_name='Лист1',
        na_values=None,
        keep_default_na=False,
    )

    return excel_data_df.to_dict('records')


def prepare_excel_data(data):
    categories = {}
    for row in data:
        categories.setdefault(row.pop('Категория'), []).append(row)
    return categories


def prepare_page(excel_data):
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('template.html')

    passed_years = date.today().year - SINCE_YEAR

    rendered_page = template.render(
        year_with_us=f'{passed_years} {declension_year(passed_years)}',
        wine_categories=prepare_excel_data(excel_data),
    )

    return rendered_page


def runserver(rendered_page):
    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == '__main__':

    excel_file = read_args().filename

    excel_data = read_excel(excel_file)
    rendered_page = prepare_page(excel_data)

    runserver(rendered_page)
