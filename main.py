import requests
import json
from flask import Flask


def get_valutes_list():
    return list((json.loads(requests.get('https://www.cbr-xml-daily.ru/daily_json.js').text))['Valute'].values())


app = Flask(__name__)


def create_html(valutes):
    text = '<html><head><title>Курсы валют</title></head>'
    text += '<body><h1>Курс валют ЦБ РФ</h1>'
    text += '<table border="1" cellpadding="5" style="border-collapse: collapse; border: 1px solid black;">'
    text += '<tr><th>Количество</th><th>Название</th><th>Курс продажи</th><th>Курс покупки</th><th>Разница курсов</th></tr>'
    for valute in valutes:
        text += '<tr>'
        for v in list(valute.values())[3:]:
            text += f'<td>{v}</td>'
        text += f'<td>{round(list(valute.values())[5] - list(valute.values())[6], 4)}</td>'
        text += '</tr>'

    text += '</table>'
    text += '</body></html>'
    return text


@app.route("/")
def index():
    valutes = get_valutes_list()
    html = create_html(valutes)
    return html


if __name__ == "__main__":
    app.run()