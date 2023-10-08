
from flask import Flask
from flask import request
from flask.views import MethodView
from flask_cors import CORS

from extension import db
from models import Poem

app = Flask(__name__)
#  跨域
CORS().init_app(app)

# 连接sqlite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///poems.db'
# 请求结束之后自动提交
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
# 跟踪修改
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# 拓展插件对象绑定到程序实例
db.init_app(app)


# @app.cli.commands()
# def create():
#     db.drop_all()
#     db.create_all()
#     Poem.init_db()
# with app.app_context():
#     db.create_all()


@app.route('/')
def hello_world():  # put application's code here
    return 'Welcome Poems!'

@app.get('/poem')
def poem_list():
    q_list = db.select(Poem).order_by(Poem.poem_id)
    poems = db.session.execute(q_list).scalars()
    return {"message":"ok", "data":[poem.json() for poem in poems]}

@app.get('/poem/<int:poem_id>')
def poem_detail(poem_id):
    poem = db.get_or_404(Poem, poem_id)

@app.get('/poem/<int:id>')
def poem_detail(id):
    poem = db.select(Poem).where(Poem.poem_id == id).first()
    return {"message":"ok", "data":poem.json()}

@app.post('/poem')
def poem_create():
    data = request.get_json()
    poem = Poem(poem_name = data.get("poem_name"),poem_author=data.get("poem_author"),poem_content=data.get("poem_content"))
    db.session.add(poem)
    db.session.commit()
    return {"message":"ok", "data":poem.json()}

@app.delete('/poem/<int:id>')
def poem_delete(id):
    poem = db.get_or_404(Poem, id)
    db.session.delete(poem)
    db.session.commit()
    return {"message":"ok"}






if __name__ == '__main__':
    app.run(debug=True)



