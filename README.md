# CI/CD Flask Demo 🚀

A minimal Flask web API containerized with Docker and deployed automatically to Docker Hub using a GitHub Actions CI/CD pipeline.  

Quick Start:

You can run the app directly from Docker Hub (replace `<your-dockerhub-username>` with your actual Docker Hub username):

bash:
docker pull <your-dockerhub-username>/ci-cd-flask:latest
docker run --rm -p 8000:8000 <your-dockerhub-username>/ci-cd-flask:latest

Test:
curl -s http://localhost:8000/        # healthcheck
expected: {"status":"ok","message":"Hello from CI/CD!"}

curl -s http://localhost:8000/sensors # simulated sensor data
expected example: {"temperature":61.2,"conveyor_speed":1.48,"anomaly":false}


