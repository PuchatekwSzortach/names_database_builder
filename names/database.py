import sqlalchemy
import sqlalchemy.ext.declarative
import sqlalchemy.orm
import sqlalchemy.event

def enforce_foreign_key_constraint(connection, record):
    connection.execute('pragma foreign_keys=ON')

engine = sqlalchemy.create_engine('sqlite:///names.db', echo=False)
sqlalchemy.event.listen(engine, 'connect', enforce_foreign_key_constraint)

Base = sqlalchemy.ext.declarative.declarative_base()


class Gender(Base):

    __tablename__ = 'genders'

    gender = sqlalchemy.Column(sqlalchemy.Unicode, primary_key=True)

    def __repr__(self):
        return self.gender


class Name(Base):

    __tablename__ = 'names'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    hiragana = sqlalchemy.Column(sqlalchemy.Unicode, nullable=False)
    kanji = sqlalchemy.Column(sqlalchemy.Unicode, nullable=False)

    gender = sqlalchemy.Column(
        sqlalchemy.Unicode, sqlalchemy.ForeignKey('genders.gender'), nullable=False)

    def __init__(self, japanese_name):

        self.hiragana = japanese_name.hiragana
        self.kanji = japanese_name.kanji
        self.gender = japanese_name.gender

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)