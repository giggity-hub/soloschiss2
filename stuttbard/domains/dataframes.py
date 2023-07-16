import pandas as pd
import os
from glob import glob
from typing import Dict

# We need to use this path, because the working directory path changes based on from where the script is executed
this_dir = os.path.dirname(__file__)
tables_dir = os.path.join(this_dir, 'extracted_tables')

def load() -> Dict[str , pd.DataFrame]:
    csv_file_paths = glob(tables_dir + '/*.csv')
    domains = {}

    for file_path in csv_file_paths:
        file_name = os.path.basename(file_path)
        domain_name, _ = os.path.splitext(file_name)

        df = pd.read_csv(file_path, sep=";")
        domains[domain_name] = df

    return domains
