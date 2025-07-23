import argparse
from src.process import clean_and_process
# from src.update import save_clean_data

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Clean inventory data")
    parser.add_argument('--input', type=str, required=True, help='Input CSV file path')
    parser.add_argument('--output', type=str, required=True, help='Output CSV file path')

    args = parser.parse_args()
    
    clean_and_process(args.input, args.output)
