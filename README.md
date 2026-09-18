\# DevSecOps Automated CI/CD Pipeline



[![DevSecOps Security Pipeline](https://github.com/ronakpandey/devsecops-pipeline/actions/workflows/devsecops-pipeline.yml/badge.svg)](https://github.com/ronakpandey/devsecops-pipeline/actions/workflows/devsecops-pipeline.yml)



A containerized Flask microservice integrated with automated security quality gates via GitHub Actions.



\---



\## Implemented Security Gates (Shift-Left)



\* \*\*Secret Detection (Gitleaks):\*\* Analyzes git commit history to detect and prevent committed credentials, private keys, and API tokens.

\* \*\*Software Composition Analysis (pip-audit):\*\* Scans Python dependencies against the Python Packaging Advisory Database for known CVEs.

\* \*\*Container Vulnerability Scanning (Trivy):\*\* Scans the built Docker container image for high and critical OS/package vulnerabilities prior to deployment.



\---



\## Local Execution



\### Run Locally

