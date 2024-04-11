from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base

# Создаем базовый класс для ORM.
Base = declarative_base()


class User(Base):
	"""Определяем класс модели User."""
	__tablename__ = 'user'

	id = Column(Integer, primary_key=True)
	tg_id = Column(Integer, unique=True)
	created = Column(DateTime, default=func.now())


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


	@classmethod
	def get_num_registered_users_today(cls, session):
		"""Возвращаем количество зарегестрированных пользователей за сегодня в боте."""
		today = func.current_date()
		num_registered_users_today = session.query(func.count(cls.id)).filter(func.DATE(cls.created) == today).scalar()
		return num_registered_users_today


	@classmethod
	def get_total_number_users(cls, session):
		"""Возвращает общее количество зарегистрированных пользователей."""
		total_users = session.query(func.count(cls.id)).scalar()
		return total_users