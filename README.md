# Distributed Log Analytics Platform

A cloud-native distributed logging platform built with:

- Kubernetes
- Apache Kafka
- OpenSearch
- Grafana
- Prometheus
- AWS EKS
- Terraform
- Argo CD

## Architecture

Applications
→ Fluent Bit
→ Kafka
→ Log Processor
→ OpenSearch
→ Grafana / Query API

## Goals

- Real-time log ingestion
- Distributed processing
- Search and analytics
- Cloud-native deployment
- GitOps workflows
- AI-powered log summaries