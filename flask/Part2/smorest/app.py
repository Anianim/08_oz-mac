from flask import Flask
from flask_smorest import Api
from api import blp

app = Flask(__name__)

# OpenAPI 관련 설정
app.config["API_TITLE"] = "My API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.1.3"
app.config["OPENAPI_URL_PREFIX"] = "/" # base url 
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui" # 실제로 open api로 만들어진 결과물 
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/" # cdn adress

api = Api(app)
api.register_blueprint(blp)

if __name__ == "__main__":
    app.run(debug=True)