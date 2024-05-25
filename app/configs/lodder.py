import os
import dvc.api
import torch

from dotenv import load_dotenv

def InitializeLogger(cls):
    cls.init_static()
    return cls

@InitializeLogger
class Lodder:
	def init_static() -> None:
		load_dotenv()

	@staticmethod
	def load_yolo_model():
		with dvc.api.open(
			'yolo.pt',
			repo='https://github.com/YU-MIDAS/project-extension.git',
			remote_config={
				'access_key_id' : os.environ.get('access_key_id'),
				'secret_access_key' : os.environ.get('secret_access_key')
			}
		) as model:
			return torch.load(model, map_location=torch.device('cpu'))
	
	@staticmethod
	def load_kcbert_model():
		with dvc.api.open(
			'kcbert_hatespeech_classifier.pth',
			repo='https://github.com/YU-MIDAS/project-extension.git',
			remote_config={
				'access_key_id' : os.environ.get('access_key_id'),
				'secret_access_key' : os.environ.get('secret_access_key')
			}
		) as model:
			return torch.load(model, map_location=torch.device('cpu'))