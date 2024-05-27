import os
import dvc.api
import torch

class Lodder:
	def __init__(self) -> None:
		self.setting_cli_config()
		self.__kcbert_model = self.load_kcbert_model('kcbert_hatespeech_classifier.pth')
		self.__yolo_model = self.load_kcbert_model('yolo.pt')

	def setting_cli_config(self):
		print(os.environ.get('ACCESS_KEY_ID'))
		print(os.environ.get('SECRET_ACCESS_KEY'))
		self.__repo = 'https://github.com/YU-MIDAS/project-extension.git'
		self.__remote_config = {
				'access_key_id' : os.environ.get('ACCESS_KEY_ID'),
				'secret_access_key' : os.environ.get('SECRET_ACCESS_KEY')
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
		

	def get_kcbert_model(self):
		return self.__kcbert_model
	
	def get_yolo_model(self):
		return self.__yolo_model