from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import Base

# Устанавливаем соединение с базой данных.
engine = create_engine('sqlite:///bot.db', echo=True)

# Create a session.
Session = sessionmaker(bind=engine)
session = Session()


def create_database():
	# Create a database if it doesn't exist.
	Base.metadata.create_all(engine)
