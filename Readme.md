# WebApp Kubernetes Template

This repo is a boilerplate template for deploying a simple Flask web app to Kubernetes (also works on OpenShift).

## 🚀 Quickstart

1. **Set the Docker image**  
   Update `k8s/deployment.yaml` with your Docker Hub user and image.

2. **Build & push**  
   ```bash
   docker build -t <your-dockerhub>/webapp:latest .
   docker push <your-dockerhub>/webapp:latest

