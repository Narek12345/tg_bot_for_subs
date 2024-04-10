from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Создаем базовый класс для ORM.
Base = declarative_base()


class User(Base):
	"""Определяем класс модели User."""
	__tablename__ = 'user'

	id = Column(Integer, primary_key=True)
	tg_id = Column(Integer, unique=True)
