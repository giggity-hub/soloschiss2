import pandas as pd
import os
from glob import glob
from typing import Dict

# We need to use this path, because the working directory path changes based on from where the script is executed
domains_dir = os.path.dirname(__file__)

def load() -> Dict[str , pd.DataFrame]:
    csv_file_paths = glob(domains_dir + '/*.csv')
    domains = {}

    for file_path in csv_file_paths:
        file_name = os.path.basename(file_path)
        domain_name, _ = os.path.splitext(file_name)

        df = pd.read_csv(file_path)
        domains[domain_name] = df

    return domains
