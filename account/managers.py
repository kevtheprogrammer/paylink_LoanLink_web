from django.contrib.auth.base_user import BaseUserManager
# from django.contrib.auth.backends import ModelBackend
# from django.contrib.auth import get_user_model

class UserManager(BaseUserManager):
	
	def create_user(self, email, password=None):
		if not email:
			raise ValueError('Users Must Have an email address')

		user = self.model(
			email=self.normalize_email(email),
		)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, password):
		"""
		Create and return a `User` with superuser (admin) permissions.
		"""
		if password is None:
			raise TypeError('Superusers must have a password.')

		user = self.create_user(email, password)
		user.is_superuser = True
		user.is_staff = True
		user.save()
		return user

	def create_client(self,email,password):
		if password is None:
			raise TypeError('Client must have a password')
		user = self.create_user(email,password)
		user.is_client = True
		user.save()
		return user


	def create_agent(self,email,password):
		if password is None:
			raise TypeError('Agent must have a password')
		user = self.create_user(email,password)
		user.is_agent = True
		user.save()
		return user
	