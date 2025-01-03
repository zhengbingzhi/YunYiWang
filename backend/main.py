from flask import Flask
from chat.chat import chat_module
from translate.translate_cmp import translate_cmp
from translate.translate import translate_module
from translate.user_info import user_info
from translate.get_info import get_info
from user.user import user
from flask_cors import CORS
from record.record import record
app = Flask(__name__)
CORS(app, supports_credentials=True, resources=r'/*')
# 注册blueprint
app.register_blueprint(chat_module)
app.register_blueprint(translate_cmp)
app.register_blueprint(translate_module)
app.register_blueprint(user)
app.register_blueprint(record)
app.register_blueprint(user_info)
app.register_blueprint(get_info)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)