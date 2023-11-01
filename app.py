import json

from collections import OrderedDict

from flask import Flask
from flask import request
from flask import jsonify
from flask import Response
from flask_cors import CORS

from sqlalchemy import func

from extension import db
from models import Poem, Poetry

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

# 建立表格
with app.app_context():
    db.create_all()


@app.route('/')
def hello_world():  # put application's code here
    return 'Welcome Poems!'

@app.get('/poem')
def poem_list():
    q_list = db.select(Poem).order_by(Poem.poem_id)
    poems = db.session.execute(q_list).scalars()
    return {"message": "ok", "data": [poem.json() for poem in poems]}


@app.get('/poem/<int:pid>')
def poem_detail(pid):
    poem = db.get_or_404(Poem, pid)
    return Response(json.dumps(poem),mimetype='application/json')


# @app.get('/poem/<int:pid>')
# def poem_detail(pid):
#     poem = db.select(Poem).where(Poem.poem_id == pid).first()
#     return {"message":"ok", "data":poem.json()}

@app.post('/poem')
def poem_create():
    data = request.get_json()
    poem = Poem(poem_name=data.get("poem_name"), poem_author=data.get("poem_author"),
                poem_dynasty=data.get("poem_dynasty"), poem_type=data.get("poem_type"),
                poem_content=data.get("poem_content"))
    db.session.add(poem)
    db.session.commit()
    return {"message": "ok", "data": poem.json()}


@app.delete('/poem/<int:pid>')
def poem_delete(pid):
    poem = db.get_or_404(Poem, pid)
    db.session.delete(poem)
    db.session.commit()
    return {"message": "ok"}

@app.get('/poetry/<string:PoetryName>')
def Poetry_biology(PoetryName):
    poetry_content = db.get_or_404(Poetry, PoetryName)
    return Response(json.dumps(poetry_content),mimetype='application/json')

#每日一诗
@app.route('/daily-poem', methods=['GET'])
def get_daily_poem():
    random_poem = Poem.query.order_by(func.random()).first()  # 从数据库中随机获取一首诗
    if random_poem:
        return jsonify({"message": "success", "data": {"title": random_poem.title, "content": random_poem.content}})
    else:
        return jsonify({"message": "error", "data": None}), 404



if __name__ == '__main__':
    app.run(debug=True)

if __name__ == '__main__':
    app.run(debug=True)

