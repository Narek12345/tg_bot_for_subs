from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Создаем базовый класс для ORM.
Base = declarative_base()


class User(Base):
	"""Определяем класс модели User."""
	__tablename__ = 'user'

	id = Column(Integer, primary_key=True)
	tg_id = Column(Integer, unique=True)


	@classmethod
	def register_user(cls, session, tg_id):
		"""Метод для регистрации пользователя."""
		existing_user = session.query(cls).filter_by(tg_id=tg_id).first()
		if existing_user:
			print("Пользователь уже зарегистрирован.")
			return existing_user
		else:
			new_user = cls(tg_id=tg_id)
			session.add(new_user)
			session.commit()
			print("Пользователь успешно зарегистрирован.")
			return new_user
