import os 
import pandas as pd

def clean():
    this_dir = os.path.dirname(__file__)
    table_path = os.path.join(this_dir, 'raw.csv')
    df = pd.read_csv(table_path)
    columns = ['name', 'area', 'number_of_steps', 'length', 'height', 'named_after']
    
    # drop all undesired columns
    df = df[columns]
    # drop rows with missing values
    df = df.dropna()

    out_path = os.path.join(this_dir, 'preprocessed.csv')
    df.to_csv(out_path, index=False)

if __name__ == "__main__":
    clean()