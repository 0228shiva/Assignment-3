import pandas as pd

def clean_and_process(input_path, output_path):
    # Load the data
    df = pd.read_csv(input_path)

    # --- Basic Cleaning Steps (you can customize this) ---

    # Strip whitespace from column names
    df.columns = df.columns.str.strip()

    # Drop fully empty rows
    df.dropna(how='all', inplace=True)

    # Fill missing values (optional example)
    df.fillna('', inplace=True)

    # Remove duplicate rows
    df.drop_duplicates(inplace=True)

    # Example: convert all column names to lowercase
    df.columns = [col.lower() for col in df.columns]

    # Save cleaned data
    df.to_csv(output_path, index=False)
    print(f"s Cleaned data saved to: {output_path}")
