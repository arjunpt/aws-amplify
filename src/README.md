# **CI/CD Pipeline for Python Static Site on AWS Amplify **

This repository implements a **CI/CD pipeline** to automate **testing**, **code analysis** and **deployment** for a Flask static site deployed on AWS Amplify. The pipeline leverages **GitHub Actions** to ensure code quality, security, and seamless deployment.

---

## **Pipeline Overview**

### **Trigger**
The pipeline is triggered by a **workflow call** with configurable inputs, such as Python version, test paths, and branch details for deployment.

### **Pipeline Stages**
1. **Code Linting (flake8)**  
   - Ensures adherence to **PEP8 coding standards**.  
   - Identifies **syntax** or **style issues** in the codebase.  
   - Generates a **lint report**, uploaded as an artifact for review.

2. **Unit Testing (pytest)**  
   - Executes unit tests using **pytest** to validate the application functionality.  
   - Generates the following reports:  
     - **Coverage Report**: Displays test coverage of the codebase.  
     - **JUnit Report**: Provides detailed test results.  
   - Both reports are uploaded as artifacts for review.

3. **Security Scan (Snyk)**  
   - Scans for vulnerabilities in the application’s dependencies using **Snyk**.  
   - Produces a **SARIF report**, uploaded as an artifact for analysis.  
   - Detects potential vulnerabilities early to ensure project security.

4. **Static Code Analysis (SonarQube)**  
   - Performs static code analysis using **SonarQube** to:  
     - Detect **code smells**.  
     - Identify **bugs** and potential issues.  
   - Enforces **SonarQube Quality Gate** to ensure code quality thresholds are met.

5. **AWS Amplify Deployment**  
   - Freezes the Flask application into static files.  
   - Starts an **AWS Amplify job** to deploy the static site.  
   - Configures branch, job type, and Amplify app details dynamically.

---
---

# **CI/CD Pipeline for AWS Glue ETL Project**


  <img src="images/architecture-amplify.png" alt="Architecture Diagram" width="70%">


---
## **Requirements**

### **Software Requirements**
- **Python 3.x**: For executing the application and tests.  
- **AWS CLI**: To interact with AWS services (e.g., Amplify).  
- **GitHub Actions**: Automates the CI/CD pipeline.  

### **Secrets Configuration**
Add the following secrets in the GitHub repository settings under `Settings > Secrets and Variables > Actions`:

| **Secret Name**       | **Description**                                      |
|------------------------|-----------------------------------------------------|
| `AWS_ACCESS_KEY`       | AWS access key ID for authentication.               |
| `AWS_SECRET_KEY`       | AWS secret access key for authentication.           |
| `AWS_REGION`           | AWS region where Amplify is deployed.               |
| `SNYK_TOKEN`           | Token for authenticating Snyk scans.                |
| `SONAR_TOKEN`          | Token for authenticating with SonarQube.            |
| `SONAR_HOST_URL`       | SonarQube server URL for static code analysis.      |
| `amplify_app_id`       | AWS Amplify application ID.                         |
| `branch-name`          | Branch name for the deployment.                     |
| `job-type`             | Type of Amplify job (e.g., release, retry, manual). |

---

## **Artifacts Generated**

| **Stage**          | **Artifact Name**      | **Description**                                    |
|---------------------|------------------------|---------------------------------------------------|
| **Linting**         | `lint-report`         | Report of linting errors and code quality.        |
| **Unit Testing**    | `coverage-report`     | HTML report of code coverage from tests.          |
| **Unit Testing**    | `junit-report`        | XML report of detailed test results.              |
| **Security Scan**   | `snyk-python-report`  | SARIF report of vulnerabilities in the code.      |

---

## **Pipeline Configuration**

### **Inputs**

| **Input Name**       | **Description**                                      |
|----------------------|-----------------------------------------------------|
| `python-version`     | Python version to set up.                           |
| `requirements-path`  | Path to the `requirements.txt` file.                |
| `test-path`          | Path to the test file or directory.                 |
| `snyk-path`          | Path to the Snyk configuration file.                |
| `amplify_app_id`     | AWS Amplify application ID.                         |
| `branch-name`        | Branch name to trigger deployment.                  |
| `job-type`           | Type of Amplify job (release, retry, manual).       |

---

## **AWS Configuration**
Ensure the following AWS resources are preconfigured:

1. **AWS Amplify Application**:  
   - Preconfigured Amplify app connected to the target branch.  
   - Update the `amplify_app_id` and `branch-name` inputs in the pipeline.

2. **AWS CLI Configuration**:  
   - Set up AWS CLI with the appropriate credentials and region in the GitHub secrets.

---

## **How to Use the Pipeline**

1. Configure the required secrets in the repository.
2. Trigger the pipeline by calling the workflow with the necessary inputs.
3. Monitor the generated artifacts and reports to ensure quality and security.
4. Verify deployment on AWS Amplify.

---

---

# **Outcomes**


  <img src="images/amplify.png" alt="Architecture Diagram" width="70%">

  <img src="images/amplify-page.png" alt="Architecture Diagram" width="70%">


---
