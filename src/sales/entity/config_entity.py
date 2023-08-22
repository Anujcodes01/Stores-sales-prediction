from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen =True)

class DataIngestionConfig:
    root_dir:Path
    source_URL_train:str
    source_URL_test :str
    train_file:Path
    test_file:Path   