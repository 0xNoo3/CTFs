FROM debian:bookworm

RUN mkdir /zadanie
WORKDIR /zadanie

COPY requirements.txt ./

RUN apt update && apt install -y python3 python3-dev python3-pip
RUN pip install --break-system-packages --extra-index-url https://download.pytorch.org/whl/cpu -r requirements.txt

COPY server.py ./
COPY kitten_detector.py ./

CMD ["gunicorn", "-b", "0.0.0.0:8000", "-w", "4", "server:app"]