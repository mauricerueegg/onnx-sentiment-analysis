import requests
import os


def download_model(url, dest_path):
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get("content-length", 0))
    block_size = 1024  # 1 Kilobyte
    wrote = 0
    with open(dest_path, "wb") as f:
        for data in response.iter_content(block_size):
            wrote = wrote + len(data)
            f.write(data)
            done = int(50 * wrote / total_size)
            print(f"\r[{'=' * done}{' ' * (50-done)}] {done * 2}%", end="")
    print()  # Newline after download completion


def ensure_model_exists(url, dest_path):
    print("checking model in folder " + os.path.abspath(dest_path))
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    if not os.path.exists(dest_path):
        print("downloading model to " + os.path.abspath(dest_path))
        download_model(url, dest_path)
