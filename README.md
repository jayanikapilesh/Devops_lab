# DevOps Lab

A collection of hands-on DevOps exercises completed as part of the **DevOps** course.

## Student Details

| Field | Value |
|---|---|
| Name | Jayani Kapilesh |
| USN | 1BM23IS114 |
| Department | Information Science and Engineering (ISE) |
| Semester | 7th Semester |
| Faculty | Prof. Sunag P & Sumukha |
| Course | DevOps |

## About This Repository

This repository documents practical exercises on core DevOps tools and concepts: containerization with Docker, orchestration with Kubernetes and Minikube, container security, monitoring and alerting, and CI/CD with Jenkins. Each exercise has its own folder containing a `README.md` with step-by-step instructions, the commands used, their outputs and screenshots, along with all code and configuration files.

All exercises were performed on **Windows 11 with Docker Desktop** (PowerShell). Where the lab instructions use Linux-specific commands, the Windows equivalents are used and the differences are explained in each exercise.

## Exercises

| # | Exercise | Description |
|---|---|---|
| 1 | [Kubernetes Getting Started – Hello Pod](Exercise-01-Kubernetes-Getting-Started) | Deploying Nginx as a Pod on a local Minikube cluster and exposing it as a NodePort Service. |
| 2 | [Deploy a Flask App on Minikube](Exercise-02-Minikube-Kubectl-Flask) | Building a Flask image inside Minikube's Docker daemon, deploying it with a Deployment, showing that it is unreachable without a Service, then exposing it with a NodePort Service. |
| 3 | [Scaling a Flask App using ReplicaSets](Exercise-03-Flash-Sale-ReplicaSet) | Running a flash sale checkout service as a ReplicaSet, scaling from 3 to 5 Pods and observing self-healing when a Pod is deleted. |
| 4 | [Docker Networking with Multiple Containers](Exercise-04-Docker-Networking) | Connecting a Flask API, MySQL and Redis on a custom bridge network and verifying name-based communication with `ping`. |
| 5 | [Docker Security with AppArmor and Python](Exercise-05-Docker-Security-AppArmor) | Applying an AppArmor profile with `docker run` and the Docker SDK for Python, including a documented platform limitation: Docker Desktop on Windows does not support AppArmor enforcement. |
| 6 | [Real-Time Operations Monitoring and Alerting](Exercise-06-Delivery-Monitoring) | Simulating delivery metrics with Python, scraping them with Prometheus, visualizing them in Grafana, firing alerts, and automating the whole stack with a Jenkins pipeline. |
| 7 | [Introduction to CI and Jenkins Installation](Exercise-07-Jenkins-CI-Automation) | Continuous Integration concepts and CI tools, plus installing and setting up Jenkins in Docker. |
| 8 | [Creating a "Hello World" Jenkins Job](Exercise-08-Jenkins-Hello-World-Job) | Pushing a shell script to GitHub and running it from a Jenkins Freestyle job. |
| 9 | [Jenkins Multi-Stage Pipeline](Exercise-09-Jenkins-Multi-Stage-Pipeline) | A Jenkinsfile with Build, Test, Deploy, Run and Test stages for a Flask app, including fixing the missing Python in the Jenkins container. |
| 10 | [Multi-Node Kubernetes Cluster with Multiple Applications](Exercise-10-Minikube-Multi-Node) | Deploying two Flask microservices across a 3-node Minikube cluster with pod anti-affinity and testing them with curl. |

## Tools Used

Docker · Kubernetes · Minikube · kubectl · Jenkins · Prometheus · Grafana · AppArmor · Python · Flask · MySQL · Redis · Git · GitHub