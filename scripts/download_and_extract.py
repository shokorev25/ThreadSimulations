import os
import requests
import zipfile

def download_and_extract():
    date = input("Enter the date (YYYY-MM-DD): ")
    link = f"https://api.simurg.space/datafiles/map_files?date={date}"
    file_name = f"{date}.zip"
    download_path = os.path.join("./data/raw", file_name)

    # Check if the zip file already exists in the raw directory
    if os.path.exists(download_path):
        print(f"File {file_name} already exists. Skipping download.")
    else:
        # Download the zip file
        with open(download_path, "wb") as f:
            print(f"Downloading {file_name}...")
            response = requests.get(link, stream=True)
            total_length = response.headers.get('content-length')
            if total_length is None: # no content length header
                f.write(response.content)
            else:
                dl = 0
                total_length = int(total_length)
                for data in response.iter_content(chunk_size=4096):
                    dl += len(data)
                    f.write(data)
                    done = int(50 * dl / total_length)
                    print(f"\r[{'=' * done}{' ' * (50 - done)}]", end='', flush=True)
        print(f"\nDownloaded {file_name} successfully.")

    # Extracting the downloaded zip file to ./data/extracted
    extract_path = "./data/extracted"
    if not os.path.exists(extract_path):
        os.makedirs(extract_path)

    with zipfile.ZipFile(download_path, 'r') as zip_ref:
        zip_ref.extractall(extract_path)
    print(f"Extracted {file_name} to {extract_path}")

if __name__ == "__main__":
    download_and_extract()
