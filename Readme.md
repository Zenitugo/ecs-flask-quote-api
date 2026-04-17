# Flask Quote API — ECS Fargate Deployment

## 📖 Overview
A simple Python Flask API that serves motivational quotes from African authors.
This project demonstrates how to deploy a containerized application on AWS ECS 
using the Fargate launch type and AWS CLI commands. No Terraform, no console 
clicking. It also covers ECR image scanning and container logging with CloudWatch.

This is Part 2 of my ECS deployment series. Part 1 covers EC2 launch type with 
Terraform: [Blog](https://dhebbydavid.hashnode.dev/deploying-your-first-containerized-application-on-aws-ecs-part-1)

## 🚀 Features
- Containerized Flask API with Gunicorn
- Deployed on AWS ECS Fargate (no EC2 instances to manage)
- ECR image scanning enabled on push
- Container logs streamed to CloudWatch Logs
- Application Load Balancer for traffic routing
- All infrastructure provisioned using AWS CLI

## 🛠 Tech Stack
- Python 3.12 + Flask + Gunicorn
- Docker
- Amazon ECR
- Amazon ECS (Fargate launch type)
- Application Load Balancer
- Amazon CloudWatch Logs
- AWS CLI

## 📂 Repo Structure
```
ecs-flask-quote-api /
├── Dockerfile
├── Readme.md
├── app.py
├── codebuild-trust-policy.json
├── codepipeline-trust-policy.json
├── ecsTaskExecutionRoleTrust.json
├── requirements.txt
└── task-def.json
```

## ⚙️ Setup Instructions

1. Clone the repo
```bash
   git clone https://github.com/Zenitugo/ecs-flask-quote-api.git
   cd ecs-flask-quote-api
```

2. Build and test locally
```bash
   docker build -t flask-quote-api .
   docker run -p 5000:5000 flask-quote-api
   curl http://localhost:5000/health
```
   > For full local testing instructions see Part 1 of this series

3. Deploy to AWS — full step by step CLI commands are documented 
   in the blog post below

## API Endpoints
| Method | Endpoint  | Description          |
|--------|-----------|----------------------|
| GET    | /health   | Health check         |
| GET    | /quote    | Get a random quote   |
| GET    | /quotes   | Get all quotes       |
| POST   | /quote    | Add a new quote      |

## 🎥 Demo
- [YouTube Walkthrough](#) (coming soon)

## 📚 Blog Post
[Full deployment walkthrough with every CLI command](https://dhebbydavid.hashnode.dev/deploying-your-containerized-application-on-aws-ecs-part-2-fargate-launch-type)

## 👤 Author
Ugochi Ukaegbu
AWS Builders Community Programme — Containers Track
[LinkedIn](https://www.linkedin.com/in/ugochiukaegbu/) | [Hashnode](https://dhebbydavid.hashnode.dev)