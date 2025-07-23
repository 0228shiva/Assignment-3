import pandas as pd

def save_clean_data(df, output_path):
    df.to_csv(output_path, index=False)
    print(f" Data saved to {output_path}")
