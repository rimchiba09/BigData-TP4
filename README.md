# TP04: Containerization and Big Data Environment Deployment Using Docker

## 1. Project Overview

This project uses Docker to containerize a Python data analysis application. The application analyzes the TalkingData mobile advertising dataset and calculates the total number of clicks, downloads, and conversion rate.

## 2. Technologies Used

- Docker
- Docker Compose
- Python 3.12
- Pandas
- TalkingData dataset

## 3. Project Structure

```text
BigData-TP04/
├── app/
│   └── app.py
├── data/
│   └── train_sample.csv
├── Dockerfile
├── compose.yaml
├── requirements.txt
└── README.md
```

## 4. Build the Docker Image

```bash
docker build -t talkingdata-analysis:v1 .
```

## 5. Run the Application

Run the container and mount the dataset directory:

```powershell
docker run --rm -v "${PWD}\data:/app/data:ro" talkingdata-analysis:v1
```

## 6. Docker Hub

The image is available on Docker Hub:

`chebarim/talkingdata-analysis:v1`

Pull the image using:

```bash
docker pull chebarim/talkingdata-analysis:v1
```

## 7. Run with Docker Compose

Build and run the application:

```bash
docker compose up --build
```

Check the container status:

```bash
docker compose ps -a
```

Stop and remove the Compose resources:

```bash
docker compose down
```

## 8. Results

The application produced the following results for `train_sample.csv`:

| Metric | Result |
|---|---:|
| Total clicks | 924,519 |
| Downloads | 2,212 |
| Conversion rate | 0.2393% |

The conversion rate is calculated as:

`Conversion Rate = (Downloads / Total Clicks) × 100`

## 9. Notes

- The dataset is mounted into the container in read-only mode.
- The application processes the CSV file in chunks to limit memory usage.
- The container exits with code 0 after completing the analysis successfully.
- Three containers were also launched from the image as part of the Docker networking task.
