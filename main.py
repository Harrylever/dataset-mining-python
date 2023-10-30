import requests
import zipfile
import io
import os

repository_url = "https://github.com/AustinWalsh/Datasets-COVID-19/archive/refs/heads/master.zip"

local_dir = "data"

os.makedirs(local_dir, exist_ok=True)

def getRepository():
    response = requests.get(repository_url)

    if response.status_code == 200:
        # print(response)
        zip_data = io.BytesIO(response.content)
        with zipfile.ZipFile(zip_data, 'r') as zip_ref:
            zip_ref.extractall(local_dir)
        print("Data exrtracted successfully")
    else:
        print("Error occured while fetch")


if __name__ == "__main__":
    print("Running script...")
    getRepository()