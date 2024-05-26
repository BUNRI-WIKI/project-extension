import os
import dvc.api
import torch

from pydantic import BaseSettings

class Settings(BaseSettings):
		ACCESS_KEY_ID: str
		SECRET_ACCESS_KEY: int

class Lodder:
	def __init__(self) -> None:
		self.setting_cli_config()

	def setting_evn_config(self, repo=None, remote_config=None, mode='rb'):
		from dotenv import load_dotenv

		load_dotenv()

		self.__repo = 'https://github.com/YU-MIDAS/project-extension.git' if repo == None else None
		self.__remote_config = {
				'access_key_id' : os.environ.get('access_key_id'),
				'secret_access_key' : os.environ.get('secret_access_key')
		} if remote_config == None else None
		self.__mode = mode
	
	def setting_cli_config(self):
		self.__repo = 'https://github.com/YU-MIDAS/project-extension.git'
		self.__remote_config = {
				'access_key_id' : os.environ('ACCESS_KEY_ID'),
				'secret_access_key' : os.environ('SECRET_ACCESS_KEY')
		}
		self.__mode = 'rb'


	def load_yolo_model(self, model_name):
		with dvc.api.open(
			model_name,
			repo=self.__repo,
			remote_config=self.__remote_config,
			mode=self.__mode
		) as model:
			return torch.load(model, map_location=torch.device('cpu'))
	
	def load_kcbert_model(self, model_name):
		with dvc.api.open(
			model_name,
			repo=self.__repo,
			remote_config=self.__remote_config,
			mode=self.__mode
		) as model:
			return torch.load(model, map_location=torch.device('cpu'))
		