# -*- coding: utf-8 -*-
from . import db
#用SQLALchemy的数据事件功能取代SQL的触发器

# ORM
class Role(db.Model):
    __tablename__='roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=True)
    users = db.relationship('User', backref='role')

    #静态方法
    @staticmethod
    def seed():
        db.session.add_all(map(lambda r: Role(name=r), ['Guest', 'Administrators']))


class User(db.Model):
    __tablename__='users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=True)
    passwd = db.Column(db.String, nullable=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    @staticmethod
    def on_created(target, value,oldvalue, initiator):
        target.role = Role.query.filter_by(name='Guests').first()


#监听属性，事件，方法
db.event.listen(User.name, 'set', User.on_created)
