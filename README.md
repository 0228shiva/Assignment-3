# RPA Inventory Project

## Overview

This project focuses on building a small RPA (Robotic Process Automation) pipeline to clean and analyze inventory data using Python. The inventory data is initially in a raw CSV format and contains missing values, duplicate records, and inconsistent formatting. The goal is to preprocess the data, generate a clean version of the dataset, and create basic visualizations to understand trends in product inventory.

## Objective

- Load and clean the raw inventory data.
- Save the cleaned version into a new CSV file.
- Analyze the inventory dataset.
- Generate visual reports using bar plots and pie charts.

## Project Structure

rpa_inventory_project/
│
├── data/
│ ├── inventory_raw.csv # Raw input dataset
│ └── clean_inventory.csv # Output file after cleaning
│
├── src/
│ ├── main.py # Script to clean the data
│ └── analyze_inventory.py # Script to generate charts and analysis
│
├── venv/ # Virtual environment folder (ignored by Git)
│
├── README.md # Project documentation
└── requirements.txt # List of required Python packages

## Installation and Setup

1. **Create and activate a virtual environment**  
   Run the following commands in the project directory:

   ```bash
   python -m venv venv

For Windows:
.\venv\Scripts\activate

Install the required packages

After activating the virtual environment, install the dependencies:
pip install pandas matplotlib seaborn

# (Optional) You can save the dependencies using:
pip freeze > requirements.txt

How to Use
1. Clean the Inventory Data
Run the following command:
python -m src.main --input data/inventory_raw.csv --output data/clean_inventory.csv

This will read the raw dataset, perform cleaning steps like:

Removing missing values

Dropping duplicates

Fixing inconsistent formatting

The cleaned data will be saved to data/clean_inventory.csv.

2. Analyze the Inventory Data
After cleaning the data, run:

python src/analyze_inventory.py

This script will generate:

Bar plots of product quantities

Pie charts showing category proportions

Other basic visual summaries

Sample Output
Cleaned data: clean_inventory.csv

Visuals: Displayed in pop-up windows using matplotlib.pyplot.show()

Notes
Be sure the folder names and paths match exactly, especially if there are spaces in folder names.

If you encounter errors related to file paths, try running commands from the root project directory.

Conclusion
This project helped me understand how to:

Work with raw CSV data using Python and pandas

Perform basic data preprocessing

Use matplotlib and seaborn for generating visual insights

Structure a Python project using virtual environments and separate modules



