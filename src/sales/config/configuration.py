from sales.constants  import *
from sales.utils.common import read_yaml , create_directories
from sales.entity.config_entity import DataIngestionConfig

class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH,
        schema_filepath = SCHEMA_FILE_PATH):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)

        create_directories([self.config.artifacts_root])

        
        
    def get_data_ingestion_config(self)->DataIngestionConfig:
        config = self.config.data_ingestion
        create_directories([config.root_dir])
                           
        data_ingestion_config = DataIngestionConfig(
            root_dir = config.root_dir,
            source_URL_train =config.source_URL_train,
            source_URL_test= config.source_URL_test,
            train_file=config.train_file,
            test_file= config.test_file,
        )
        return data_ingestion_config