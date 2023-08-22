import os 
import urllib.request as requests
from sales import logger
from sales.utils.common import get_size
from pathlib import Path
from sales.entity.config_entity import DataIngestionConfig


class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config = config
        
    def download_file_train(self):
        if not os.path.exists(self.config.train_file):
            filename, headers = requests.urlretrieve(
                url = self.config.source_URL_train,
                filename = self.config.train_file
            )
            logger.info(f"{filename} download! with following info: \n{headers}")
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.train_file))}")
            
    def download_file_test(self):
        if not os.path.exists(self.config.test_file):
            filename, headers = requests.urlretrieve(
                url = self.config.source_URL_test,
                filename = self.config.test_file
            )
            logger.info(f"{filename} download! with following info: \n{headers}")
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.test_file))}")
   