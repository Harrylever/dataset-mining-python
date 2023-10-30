import requests
import zipfile
import pandas as pd
import io

# repository_url = "https://github.com/AustinWalsh/Datasets-COVID-19/archive/refs/heads/master.zip"
# csv_file_name = "NYT-us-counties.csv"

repository_url = input("Please enter the repository zip URL: ")
csv_file_name = input("Please enter the csv file name to search: ")

zip_url = repository_url

def getRepoAndCSV():
    response = requests.get(zip_url)
    df = None
    if response.status_code == 200:
        with zipfile.ZipFile(io.BytesIO(response.content)) as zip_ref:
            for file_info in zip_ref.infolist():
                if csv_file_name in file_info.filename:
                    with zip_ref.open(file_info) as csv_file:
                        df = pd.read_csv(csv_file)
                    break

    if df is not None:
        print("CSV loaded successfully...")
        print(df)
    else:
        print("CSV could not be loaded")


if __name__ == "__main__":
    print("Running script....")
    getRepoAndCSV()