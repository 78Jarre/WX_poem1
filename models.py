from extension import db


#  定义模型
class Poem(db.Model):
    __tablename__ = 'poem'
    poem_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    poem_name = db.Column(db.String(255), unique=True)
    poem_author = db.Column(db.String(255), nullable=False)
    poem_dynasty = db.Column(db.String(255), nullable=False)
    poem_type = db.Column(db.Integer, nullable=False)
    poem_content = (db.Column(db.Text))

    def __init__(self, poem_name, poem_author, poem_dynasty, poem_type, poem_content):
        self.poem_name = poem_name
        self.poem_author = poem_author
        self.poem_dynasty = poem_dynasty
        self.poem_type = poem_type
        self.poem_content = poem_content

    def __repr__(self):
        return '<Poem %r>' % self.poem_name

    def json(self):
        return {
            'poem_id': self.poem_id,
            'poem_name': self.poem_name,
            'poem_author': self.poem_author,
            'poem_dynasty': self.poem_dynasty,
            'poem_type': self.poem_type,
            'poem_content': self.poem_content
        }
