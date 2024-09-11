import requests
from pathlib import Path

def download_to_local(url, destination_out_path, parent_mkdir:bool=True):
    if not isinstance(destination_out_path, Path):
        raise ValueError(f"{destination_out_path} must be a valid pathlib.path object")
    if parent_mkdir:
        destination_out_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        response = requests.get(url)
        response.raise_for_status()

        # write the file out in binary mode to prevent any newline conversions
        destination_out_path.write_bytes(response.content)
        return True
    except requests.RequestException as e:
        print(f"failed to download {url}: {e}")
        return False