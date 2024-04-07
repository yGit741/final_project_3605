# Twitter Data Analysis Project

## Overview
This project aims to source real-time Twitter data for comprehensive analysis using a Kubernetes cluster. The project includes data acquisition, Kubernetes cluster configuration, data ingestion and processing, data analysis, insight visualization, and an executive summary of the findings.

## Project Structure

### Tasks

1. **data_ingestion**: make the authentication process with the tweeter API. due to problems with the versions, as adviced in the piazza we will use the toy kaggle dataset (saved as tweets_df.csv).
2. **Ddata_processing**: make the cleaning and integrity check of the data and save it in the data folder as tweets_df_.csv.processed
3. **data_analysis_microservice**: the main service that make analysis including descriptive statistics, trends and visualizations.

### How to run it?
   - Navigate to the directory containing the Dockerfile.
   - Build the Docker image using the command: `docker build -t tweeter-app .`
   - Apply the Deployment configuration: `kubectl apply -f deployment.yaml`
   - Monitor the deployment status: `kubectl rollout status deployment/my-deployment`
   - To handle increased load, scale the number of pods: `kubectl scale deployment/my-deployment --replicas=3`
   - Verify the scaling: `kubectl get pods`
   - To remove the deployed resources: `kubectl delete -f deployment.yaml -f service.yaml

