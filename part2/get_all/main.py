# У вас имеется настроенный фласк и словарь с данными.
#
# Вам необходимо:
#
# 1. Создать переменную app c экземпляром
#    класса App из библиотеки flask_restx
#
# 2. Создать неймспейc book_ns с адресом `/books`
#
# 3. Создать Сlass based view который позволяет
#    с помощью GET-запроса по адресу `/books` получить
#    список всех сущностей, определенных в cписке


from flask import Flask
from flask_restx import Api, Resource

app = Flask(__name__)

api = Api(app)
book_ns = api.namespace('books')

books = [
    {
        "id": 1,
        "name": "Harry Potter",
        "year": 2000,
        "author": "Joan Routing"
    },
    {
        "id": 2,
        "name": "Le Comte de Monte-Cristo",
        "year": 1844,
        "author": "Alexandre Dumas"
    }
]


@book_ns.route('/')
class BooksView(Resource):
    def get(self):
        return books, 200


# для проверки работоспособности запустите фаил
# и зайдите в браузере на адрес http://127.0.0.1/books

if __name__ == '__main__':
    app.run(debug=False)
