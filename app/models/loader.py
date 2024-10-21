import os
from dotenv import load_dotenv

import torch

from app.utils.logger import Logger

load_dotenv()

class S3ModelLoader:
    def __init__(self):
        """
        Initialize S3ModelLoader with AWS session and cache directory.

        Parameters:
        cache_dir (str): Local directory where the downloaded models will be cached.

        """
        import boto3

        Logger.info("Initializing S3ModelLoader...")
        session = boto3.Session(
            aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
            aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
            region_name=os.getenv("AWS_DEFAULT_REGION")
        )
        
        self.s3 = session.resource("s3")
        self.bucket_name = os.getenv("AWS_S3_BUCKET_NAME")
        self.cache_dir = os.path.abspath(os.getenv("MODELS_DIRS"))

        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        Logger.info(f"Using device: {self.device}")
        Logger.info("S3ModelLoader initialized successfully.")


    def _get_latest_model_path_from_s3(self):
        """
        Fetch the latest model paths from S3's `latest_model.yaml`.

        Returns:
        dict: A dictionary containing the latest model paths and metadata from S3.

        """
        import yaml

        Logger.info("Fetching the latest model path from S3...")
        obj = self.s3.Object(self.bucket_name, "models/latest_model.yaml")
        Logger.info("Fetched latest model information successfully.")
        return yaml.safe_load(obj.get()["Body"].read())


    def _download_model_from_s3(self, model_name, s3_key):
        """
        Download a model from S3 and cache it locally.

        If a file with the same name exists in the cache directory, it will be
        automatically overwritten by the new download.

        Parameters:
        model_name (str): Name of the model to be downloaded and cached.
        s3_key (str): S3 key (path) of the model file to be downloaded.

        Returns:
        str: The local path of the downloaded model.

        """
        local_path = os.path.join(self.cache_dir, model_name)

        os.makedirs(self.cache_dir, exist_ok=True)

        # Download the new model from S3 and overwrite the file if it exists
        Logger.info(f"Downloading {model_name} from S3 (bucket: {self.bucket_name}, key: {s3_key})...")
        print(self.bucket_name, s3_key, local_path)
        self.s3.Bucket(self.bucket_name).download_file(s3_key, local_path)
        Logger.info(f"Downloaded {model_name} to {local_path} successfully.")

        return local_path


    def load_kcbert_model(self):
        """
        Download and load the KcBERT model and tokenizer from S3.

        Downloads the latest KcBERT model and tokenizer from S3 and loads
        them into memory for use.

        Returns:
        tuple: A tuple containing the loaded KcBERT model and tokenizer.

        """
        Logger.info("Loading KcBERT model from S3...")
        latest_kcbert_model_info = self._get_latest_model_path_from_s3()["models"]["kcbert"]
        name = latest_kcbert_model_info["name"]
        path = latest_kcbert_model_info["path"]
        
        from transformers import AutoTokenizer, AutoModelForSequenceClassification

        Logger.info("Loading KcBERT base model and tokenizer from local...")
        base_model_name = "beomi/kcbert-base"
        model = AutoModelForSequenceClassification.from_pretrained(base_model_name, num_labels=11)
        tokenizer = AutoTokenizer.from_pretrained(base_model_name)

        Logger.info(f"Downloading latest KcBERT model state_dict from S3: {name}")
        local_state_dict_path = self._download_model_from_s3(name, path)

        Logger.info("Loading state_dict into the KcBERT model...")
        state_dict = torch.load(local_state_dict_path, map_location=self.device)
        model.load_state_dict(state_dict)
        model.eval()

        Logger.info("KcBERT model loaded successfully.")
        return model, tokenizer


    def load_yolo_model(self):
        """
        Download and load the YOLO model from S3.

        Downloads the latest YOLO model state_dict from S3 and loads it into memory
        for use.

        Returns:
        YOLO: The YOLO model loaded with the latest state_dict.

        """
        Logger.info("Loading YOLO model from S3...")
        latest_yolo_model_info = self._get_latest_model_path_from_s3()["models"]["yolo"]
        name = latest_yolo_model_info["name"]
        path = latest_yolo_model_info["path"]

        from ultralytics import YOLO
        
        Logger.info(f"Downloading latest YOLO model state_dict from S3: {name}")
        local_model_path = self._download_model_from_s3(name, path)

        Logger.info("Initializing the YOLO model...")
        model = YOLO(local_model_path)

        Logger.info("YOLO model loaded successfully.")
        return model
