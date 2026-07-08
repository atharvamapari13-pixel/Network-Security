import os
import sys
import numpy as np
import pandas as pd

TARGET_COLUMN="Result"
PIPELINE_NAME="NetworkSecurity"
ARTIFACT_DIR: str = "Artifacts"
FILE_NAME: str = "NetworkData.csv"

TRAIN_FILE_NAME: str = "train.csv"
TEST_FILE_NAME: str = "test.csv"


DATA_INGESTION_COLLECTION_NAME: str  = "NetworkData"
DATA_INGESTION_DATABASE_NAME: str  = "Atharva"
DATA_INGESTION_DIR_NAME: str  = "data_ingestion"
DATA_INGESTION_FUTURE_STORE_NAME: str  = "feature_store"
DATA_INGESTION_INGESTED_DIR: str  = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATION: float  = 0.2


