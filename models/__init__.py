import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base

SCOPE_PUBLIC = 0
SCOPE_PRIVATE = 1

Base = declarative_base()

class ChatHistory(Base):
    __tablename__ = 'chat_history'
    id = sa.Column(sa.Integer, primary_key=True)
    username = sa.Column(sa.String(80), nullable=False)
    name = sa.Column(sa.String(80), nullable=False)
    message = sa.Column(sa.Text, nullable=False)
    created_at = sa.Column(sa.DateTime, nullable=False)

    def __repr__(self):
        return '<ChatHistory %r>' % self.name

class Profile(Base):
    __tablename__ = 'profile'
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(100), nullable=False)
    displayName = sa.Column(sa.String(100), nullable=False)
    avatar = sa.Column(sa.String(100), nullable=False)
    bot = sa.Column(sa.String(100), nullable=False)
    description = sa.Column(sa.Text, nullable=False)
    message = sa.Column(sa.Text, nullable=False)
    offline = sa.Column(sa.Integer, nullable=False)
    deleted = sa.Column(sa.Integer, nullable=False)
    owned_by = sa.Column(sa.String(100), nullable=False)
    scope = sa.Column(sa.Integer, nullable=False)

class User(Base):
    __tablename__ = 'user'
    id = sa.Column(sa.Integer, primary_key=True)
    username = sa.Column(sa.String(100), nullable=False)
    displayName = sa.Column(sa.String(100), nullable=False)
    password = sa.Column(sa.String(100), nullable=False)
    avatar = sa.Column(sa.String(100), nullable=False)
    description = sa.Column(sa.Text, nullable=True)
    invitation_code = sa.Column(sa.String(100), nullable=True)
    invitation_count = sa.Column(sa.Integer, nullable=False)

class User_Profile_Rel(Base):
    __tablename__ = 'user_profile_rel'
    id = sa.Column(sa.Integer, primary_key=True)
    username = sa.Column(sa.String(100), nullable=False)
    profile_name = sa.Column(sa.String(100), nullable=False)
    last_chat_at = sa.Column(sa.DateTime, nullable=False)
    number_of_chats = sa.Column(sa.Integer, nullable=False)
    relations = sa.Column(sa.Integer, nullable=False)  #0: stranger, 1: friends, 2: close friends
    