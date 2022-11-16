from flask import Flask, request, jsonify


class FlaskExercise:
    """
    Вы должны создать API для обработки CRUD запросов.
    В данной задаче все пользователи хранятся в одном словаре, где ключ - это имя пользователя,
    а значение - его параметры. {"user1": {"age": 33}, "user2": {"age": 20}}
    Словарь (dict) хранить в памяти, он должен быть пустым при старте flask.

    POST /user - создание пользователя.
    В теле запроса приходит JSON в формате {"name": <имя пользователя>}.
    Ответ должен вернуться так же в JSON в формате {"data": "User <имя пользователя> is created!"}
    со статусом 201.
    Если в теле запроса не было ключа "name", то в ответ возвращается JSON
    {"errors": {"name": "This field is required"}} со статусом 422

    GET /user/<name> - чтение пользователя
    В ответе должен вернуться JSON {"data": "My name is <name>"}. Статус 200

    PATCH /user/<name> - обновление пользователя
    В теле запроса приходит JSON в формате {"name": <new_name>}.
    В ответе должен вернуться JSON {"data": "My name is <new_name>"}. Статус 200

    DELETE /user/<name> - удаление пользователя
    В ответ должен вернуться статус 204
    """

    @staticmethod
    def configure_routes(app: Flask) -> None:
        users: dict = {}

        @app.post("/user")
        def create_user() -> tuple:
            request_data = request.get_json()

            if "name" in request_data:
                username = request_data["name"]
                del request_data["name"]
                users[username] = request_data

                data_to_return = {"data": f"User {username} is created!"}

                return jsonify(data_to_return), 201

            errors = {"errors": {"name": "This field is required"}}

            return jsonify(errors), 422

        @app.get("/user/<name>")
        def get_user(name: str = None) -> tuple:
            if name in users:
                data_to_return = {"data": f"My name is {name}"}

                return jsonify(data_to_return), 200

            return "", 404

        @app.patch("/user/<name>")
        def patch_user(name: str = None) -> tuple:
            if name in users:
                request_data = request.get_json()

                new_name = request_data["name"]
                users[new_name] = users[name]
                del users[name]

                data_to_return = {"data": f"My name is {new_name}"}

                return jsonify(data_to_return), 200

            return "", 404

        @app.delete("/user/<name>")
        def delete_user(name: str = None) -> tuple:
            if name in users:
                del users[name]

                return "", 204

            return "", 404
