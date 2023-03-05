from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def config_database(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()


# define Models here

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(512), nullable=False)
    password = db.Column(db.String(512), nullable=False)

    def to_json(self):
        return {
            'id': self.id,
            'username': self.username,
            'password': self.password
        }
