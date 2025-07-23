import pandas as pd
import logging

def load_inventory(file_path):
    logging.info(f"Loading inventory from {file_path}")
    return pd.read_csv(file_path)
