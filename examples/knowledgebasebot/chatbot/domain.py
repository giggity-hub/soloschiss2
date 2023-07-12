import os
import pandas as pd

def load_domains():
    domain_dir = '../domain'

    csv_file_names = os.listdir(domain_dir)
    csv_file_paths = [os.path.join(domain_dir, name) for name in csv_file_names]
    object_types = [os.path.splitext(name)[0] for name in csv_file_names]
    dfs = [pd.read_csv(file_path) for file_path in csv_file_paths]

    return dict(zip(object_types, dfs))

domains = load_domains()