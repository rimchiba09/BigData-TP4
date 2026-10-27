
import pandas as pd
from pathlib import Path

DATA_FILE = Path("/app/data/train_sample.csv")
CHUNK_SIZE = 100_000

def main():
    if not DATA_FILE.exists():
        raise FileNotFoundError(f"Dataset not found: {DATA_FILE}")

    total_clicks = 0
    total_downloads = 0

    print("Starting TalkingData analysis...")
    print(f"Dataset: {DATA_FILE.name}")

    for chunk in pd.read_csv(DATA_FILE, chunksize=CHUNK_SIZE):
        total_clicks += len(chunk)
        total_downloads += int(chunk["is_attributed"].sum())

    conversion_rate = (
        total_downloads / total_clicks * 100
        if total_clicks else 0
    )

    print("\nAnalysis Results")
    print("------------------------------")
    print(f"Total clicks: {total_clicks:,}")
    print(f"Downloads: {total_downloads:,}")
    print(f"Conversion rate: {conversion_rate:.4f}%")
    print("------------------------------")
    print("Analysis completed successfully.")

if __name__ == "__main__":
    main()
