FROM jjanzic/docker-python3-opencv

RUN apt-get update && apt-get install -y python3-dev gcc \
    && rm -rf /var/lib/apt/lists/*
    
COPY . .

RUN pip install -r requirements.txt

CMD ["python", "live.py"]
