@echo off
echo Building PCC Flag Generator...
docker build -t pcc-flag-generator .

echo Starting container...
docker run -d -p 8080:8080 --name pcc-challenge pcc-flag-generator

echo Application running at: http://localhost:8080
echo To stop: docker stop pcc-challenge
echo To remove: docker rm pcc-challenge