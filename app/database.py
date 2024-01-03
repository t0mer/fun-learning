from sqlalchemy import create_engine
import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from letters import Letter

engine = db.create_engine("mysql+pymysql://root:T0mer!2405-77@localhost/tags", echo=True)
connection = engine.connect()
metadata = db.MetaData()
numbers = db.Table('numbers', metadata, autoload=True, autoload_with=engine)
query = db.select([numbers])
print(query)
ResultProxy = connection.execute('SELECT Id, NumberId, Number from numbers')
ResultSet = ResultProxy.fetchall()
english_letters= []
for row in ResultSet:
    english_letters.append(Letter(row[0],row[1],row[2]))
print(english_letters[0].Id)
for column_name in ResultProxy._metadata.keys:
    print(column_name)