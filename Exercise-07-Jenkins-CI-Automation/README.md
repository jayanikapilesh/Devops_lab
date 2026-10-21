# Exercise 7: Introduction to Continuous Integration (CI) and Jenkins Installation

## Objective

Understand the concept of Continuous Integration (CI), explore popular CI tools, and install Jenkins using Docker.

## Technologies Used

- Docker Desktop
- Jenkins (LTS) Docker image
- PowerShell
- Web browser

---

## What is Continuous Integration (CI)?

Continuous Integration is a software development practice in which developers merge their code changes into a shared repository frequently. Every merge is automatically built and tested, so integration problems are found early instead of piling up until release. This improves software quality and speeds up delivery.

## Key Features of CI

1. **Frequent Code Integration:** Developers commit small changes to the shared repository several times a day.
2. **Automated Builds:** Each commit triggers an automatic build that checks whether the code still compiles and packages correctly.
3. **Automated Testing:** Automated tests run as part of every build to confirm existing functionality has not broken.
4. **Immediate Feedback:** Developers are notified of build and test results quickly, so they can fix issues while the change is still fresh.

## Benefits of CI

- **Early Bug Detection:** Integration issues are caught soon after they are introduced, when they are cheapest to fix.
- **Improved Collaboration:** Everyone works on the same up-to-date codebase, which reduces merge conflicts.
- **Faster Development Cycles:** Automation removes repetitive manual build and test work.
- **High-Quality Code:** Continuous testing prevents regressions from reaching later stages.

## How CI Works

1. **Developer Workflow:** A developer writes code and pushes it to a version control system such as Git.
2. **CI Server Workflow:** The CI server (for example Jenkins or GitLab CI) detects the change and starts a build.
3. **Automated Build:** Dependencies are resolved and the application is compiled and packaged.
4. **Automated Testing:** Unit, integration and other automated tests verify the application.
5. **Feedback:** The success or failure result is reported back to the developer.

## Example of CI Tools

### 1. GitLab CI/CD
- **Overview**: CI/CD built into the GitLab platform.
- **Key Features**:
  - Built into GitLab.
  - YAML pipelines.
  - Auto DevOps.
- **Ideal For**: Teams using GitLab.
- **Website**: [https://gitlab.com](https://gitlab.com)

---

### 2. CircleCI
- **Overview**: Cloud-based CI/CD service.
- **Key Features**:
  - Container-based execution.
  - Parallelism and caching.
  - Native Docker support.
- **Ideal For**: Container-heavy workflows.
- **Website**: [https://circleci.com](https://circleci.com)

---

### 3. Travis CI
- **Overview**: Hosted CI service popular with open source.
- **Key Features**:
  - YAML configuration.
  - Many languages supported.
  - GitHub integration.
- **Ideal For**: Open-source projects and small teams.
- **Website**: [https://travis-ci.org](https://travis-ci.org)

---

### 4. Bamboo
- **Overview**: Atlassian's CI/CD server.
- **Key Features**:
  - Build and deployment pipelines.
  - JIRA/Confluence/Bitbucket integration.
- **Ideal For**: Teams in the Atlassian ecosystem.
- **Website**: [https://www.atlassian.com/software/bamboo](https://www.atlassian.com/software/bamboo)

---

### 5. TeamCity
- **Overview**: JetBrains CI/CD server.
- **Key Features**:
  - Detailed build history.
  - Pre-built runners.
  - Docker and Kubernetes plugins.
- **Ideal For**: Complex enterprise setups.
- **Website**: [https://www.jetbrains.com/teamcity](https://www.jetbrains.com/teamcity)

---

### 6. Azure DevOps Pipelines
- **Overview**: Microsoft's CI/CD service.
- **Key Features**:
  - Azure and Visual Studio integration.
  - YAML or classic editor.
  - Multi-platform.
- **Ideal For**: Teams on Azure.
- **Website**: [https://azure.microsoft.com/en-us/services/devops/](https://azure.microsoft.com/en-us/services/devops/)

---

### 7. GitHub Actions
- **Overview**: CI/CD built into GitHub.
- **Key Features**:
  - YAML workflows.
  - Actions marketplace.
  - Deep GitHub integration.
- **Ideal For**: Teams using GitHub.
- **Website**: [https://github.com/features/actions](https://github.com/features/actions)

---

### 8. Spinnaker
- **Overview**: Open-source continuous delivery platform.
- **Key Features**:
  - Multi-cloud deployment.
  - Kubernetes/AWS/GCP support.
  - Canary and blue-green releases.
- **Ideal For**: Cloud-native deployments.
- **Website**: [https://spinnaker.io](https://spinnaker.io)

---

### 9. Buildkite
- **Overview**: Hybrid CI/CD platform.
- **Key Features**:
  - Cloud management with self-hosted agents.
  - Parallel builds.
- **Ideal For**: Teams with strict security needs.
- **Website**: [https://buildkite.com](https://buildkite.com)

---

### 10. Drone
- **Overview**: Lightweight container-based CI/CD.
- **Key Features**:
  - Each pipeline step runs in a Docker container.
  - Open source.
  - Git provider integration.
- **Ideal For**: Container-first teams.
- **Website**: [https://www.drone.io](https://www.drone.io)

---

## CI Workflow Example

1. **Code Change:** A developer pushes code to a Git repository.
2. **Trigger Build:** The CI server detects the push and starts a build.
3. **Run Tests:** Automated tests validate the new code.
4. **Feedback:** The developer receives the build and test results.

---

# Introduction to Jenkins

## What is Jenkins?

Jenkins is an open-source automation server used to build, test and deploy software. It automates the repetitive parts of the development process and supports both Continuous Integration (CI) and Continuous Delivery (CD).

## Why Use Jenkins?

- **Automation:** Removes repetitive manual tasks from the build and release process.
- **Continuous Integration:** Verifies that code changes integrate smoothly.
- **Extensibility:** Thousands of plugins connect Jenkins to other tools and services.
- **Scalability:** Builds can be distributed across multiple machines.

## Key Jenkins Concepts

1. **Job/Project:** A task or process that Jenkins runs.
2. **Build:** One run of a job, such as compiling and packaging code.
3. **Pipeline:** A series of stages to build, test and deploy an application.
4. **Plugins:** Add-ons that extend Jenkins (for example the Git or Docker plugin).
5. **Nodes:** Machines on which Jenkins runs jobs (controller/agent setup).

---

## Getting Started with Jenkins

### 1. Install Jenkins using Docker

**Command:**

```powershell
docker run -d --name jenkins -p 8080:8080 -p 50000:50000 jenkins/jenkins:lts
```

- `-d` runs the container in the background.
- `--name jenkins` names the container `jenkins`.
- `-p 8080:8080` exposes the Jenkins web interface on host port `8080`.
- `-p 50000:50000` exposes the port used for agent communication.

Note: External Access is port **8080**

### Output

```text
PS C:\Users\Jayani Kapilesh\Desktop\devops lab> docker run -d --name jenkins -p 8080:8080 -p 50000:50000 jenkins/jenkins:lts
3a1bc12f93da1da39051c871a693a99b8fb449a233695e808d7cbe3d16f91af6
```

The `jenkins/jenkins:lts` image was already available locally, so Docker started the container directly and printed the container ID.

**Issue faced:** The first attempt failed with `Bind for 0.0.0.0:8080 failed: port is already allocated`. Checking with `docker ps --filter "publish=8080"` showed that an old `cadvisor` container was using port `8080`. It was stopped with `docker stop cadvisor`, the failed container was removed with `docker rm -f jenkins`, and the `docker run` command was run again successfully.

![Jenkins docker run](screenshots/01-jenkins-docker-run.png)

### Get Jenkins Initial Password

#### Verify the Jenkins Container

**Command:**

```powershell
docker ps -a
```

**Output:**

```text
CONTAINER ID   IMAGE                 COMMAND                  CREATED         STATUS         PORTS                                                                                          NAMES
3a1bc12f93da   jenkins/jenkins:lts   "/usr/bin/tini -- /u…"   2 minutes ago   Up 2 minutes   0.0.0.0:8080->8080/tcp, [::]:8080->8080/tcp, 0.0.0.0:50000->50000/tcp, [::]:50000->50000/tcp   jenkins
```

The output confirmed that the `jenkins` container was running from the `jenkins/jenkins:lts` image, with ports `8080` and `50000` mapped to the host.

![Jenkins container running](screenshots/02-docker-ps.png)

#### Retrieve the Initial Admin Password

Opened a shell inside the Jenkins container:

**Command:**

```powershell
docker exec -it jenkins bash
```

Displayed the initial admin password:

**Command:**

```bash
cat /var/jenkins_home/secrets/initialAdminPassword
```

The password was copied for the unlock step and then the container shell was closed with `exit`. The password is not included in this documentation for security reasons.

### Access Jenkins on Port 8080

Opened Jenkins in the browser:

```text
http://localhost:8080/
```

The **Unlock Jenkins** screen appeared, and the initial admin password was entered.

### Installation Screens

#### Unlock Jenkins

![Unlock Jenkins](screenshots/03-jenkins-unlock.png)

#### Getting Started – Customize Jenkins

The **Customize Jenkins** screen offered two options. **Install suggested plugins** was selected.

![Customize Jenkins](screenshots/04-jenkins-getting-started.png)

#### Getting Started – Install Suggested Plugins

Jenkins installed the commonly used plugins such as Folders, Pipeline, Git, Credentials Binding and Workspace Cleanup. The progress bar and plugin status were shown on the **Getting Started** screen.

![Plugins installing](screenshots/05-plugins-installing.png)

#### Create First Admin User

Created an administrator account to log in to Jenkins. Login credentials are not included in this documentation.

![Create admin user](screenshots/06-create-admin-user.png)

#### Instance Configuration

The default Jenkins URL `http://localhost:8080/` was kept, since Jenkins is accessed from the same machine.

![Instance configuration](screenshots/07-instance-configuration.png)

#### Jenkins is Ready

Jenkins showed the setup completion screen. **Start using Jenkins** was selected.

![Jenkins is ready](screenshots/08-jenkins-ready.png)

#### Jenkins Landing Page

The Jenkins dashboard opened with the **Welcome to Jenkins!** page, confirming that Jenkins 2.580.1 was installed and ready to use.

![Jenkins landing page](screenshots/09-jenkins-landing-page.png)

---

## Result

Studied the concepts, features, benefits and workflow of Continuous Integration and compared ten popular CI tools. Installed Jenkins LTS (version 2.580.1) in a Docker container, resolved a port `8080` conflict, verified the container and its port mappings, unlocked Jenkins with the initial admin password, installed the suggested plugins, created an admin user and reached the Jenkins dashboard at `http://localhost:8080/`. The Jenkins container was kept running for use in later exercises.