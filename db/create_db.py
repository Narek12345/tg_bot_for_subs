from sqlalchemy import create_engine

from db.models import Base

# Устанавливаем соединение с базой данных.
engine = create_engine('sqlite:///bot.db', echo=True)


def create_database():
	# Create a database if it doesn't exist.
	Base.metadata.create_all(engine)
