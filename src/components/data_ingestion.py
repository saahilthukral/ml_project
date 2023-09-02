import os
import sys
from src.logger import logging
from src.exception import CustomException
import pandas as pd
from sklearn.model_selection import train_test_split


from dataclasses import dataclass


#Some inputs required written in this
@dataclass
class DataIngestionConfig:
    train_data_path: str=os.path.join("artifacts", "train.csv")
    test_data_path: str=os.path.join("artifacts", "test.csv")
    raw_data_path: str=os.path.join("artifacts", "data.csv")

class DataIngestion:
    def __init__(self) -> None:
        self.ingestion_config = DataIngestionConfig()
    
    def ingestion(self):
        logging.info("Data Ingestion Phase")
        try:
            df = pd.read_csv("notebook/data/stud.csv")
            logging.info("Read the dataset")
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok= True)

            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            logging.info("Train test split initiated")

            X_train, X_test = train_test_split(df,test_size=0.2, random_state=45)

            X_train.to_csv(self.ingestion_config.train_data_path, index = False, header = True)
            X_test.to_csv(self.ingestion_config.test_data_path, index = False, header = True)

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path,

            )

        except Exception as e:
            raise(CustomException, sys)
        

        if __name__ == "__main__":
            obj = DataIngestion()
            obj.ingestion()