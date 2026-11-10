
from flask import Flask, jsonify, request
import time

app = Flask(__name__)
app.json.ensure_ascii = False


# Данные пользователей
users = [
    {"id": 1, "name": "Иван", "age": 22},
    {"id": 2, "name": "Анна", "age": 24},
    {"id": 3, "name": "Алексей", "age": 21}
]


# Данные компаний
companies = [
    {"id": 1, "name": "TechSoft", "city": "Москва"},
    {"id": 2, "name": "DataLab", "city": "Санкт-Петербург"},
    {"id": 3, "name": "WebSystems", "city": "Казань"}
]


# Логирование входящих HTTP-запросов
@app.before_request
def log_request():
    print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {request.method} {request.path}")


# 1. Главная страница
@app.route('/')
def home():
    return "Добро пожаловать на мой сервер!"


# 2. Список всех пользователей
@app.route('/api/users')
def get_users():
    return jsonify(users)


# 3. Список всех компаний
@app.route('/api/companies')
def get_companies():
    return jsonify(companies)


# 4. Получение пользователя по ID
@app.route('/api/users/<int:user_id>')
def get_user(user_id):
    for user in users:
        if user["id"] == user_id:
            return jsonify(user)

    return jsonify({"error": "Пользователь не найден"}), 404


# 5. Обработка ошибки 404
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not Found"}), 404


if __name__ == '__main__':
    app.run(port=3000, debug=True)
