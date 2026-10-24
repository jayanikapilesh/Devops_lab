# Exercise 1: Kubernetes Getting Started — Hello Pod

## 1. Aim

To deploy an Nginx web server on Kubernetes using Minikube, expose it through a NodePort Service, and access the application through a web browser.

## 2. Problem Statement

A quick-commerce platform such as Zepto needs its web application to be deployed and accessible to users. Kubernetes can manage application containers, while Services provide a way to access deployed applications.

In this experiment, an Nginx container is deployed as a Kubernetes Pod and exposed through a NodePort Service.

## 3. Environment and Tools

| Component | Details |
|---|---|
| Operating System | Windows 11 |
| Container Platform | Docker Desktop |
| Kubernetes Environment | Minikube |
| Kubernetes CLI | kubectl |
| Web Server | Nginx |
| Minikube Driver | Docker |
| Terminal | PowerShell |
| Editor | Visual Studio Code |

## 4. Prerequisites

- Docker Desktop installed and running.
- Minikube installed.
- kubectl installed.
- Internet connection to download the Nginx image.

## 5. Implementation Steps

### Step 1: Start Minikube

Start the local Kubernetes cluster using the Docker driver.

```powershell
minikube start --driver=docker
```

![Minikube startup](screenshots/01-minikube-start.png)

### Step 2: Verify the Kubernetes Node

Check whether the Minikube node is ready.

```powershell
kubectl get nodes
```

The node should display `Ready` status.

![Kubernetes node ready](screenshots/02-cluster-ready.png)

### Step 3: Deploy the Nginx Pod

Create a Pod named `hello-k8s` using the Nginx image and specify port 80.

```powershell
kubectl run hello-k8s --image=nginx --port=80
```

Verify that the Pod is running.

```powershell
kubectl get pods -o wide
```

The Pod should show `1/1` under READY and `Running` under STATUS.

![Nginx Pod running](screenshots/03-pod-running.png)

### Step 4: Expose the Pod Using a NodePort Service

Expose the Pod so that the application can be accessed through a Kubernetes Service.

```powershell
kubectl expose pod hello-k8s --type=NodePort --port=80
```

Check the available Services.

```powershell
kubectl get services
```

The output displays the Service type as `NodePort` and maps port 80 to a NodePort.

![NodePort service](screenshots/04-service.png)

### Step 5: Access the Application

Run the following command to open the Service through Minikube.

```powershell
minikube service hello-k8s
```

Minikube provides a URL and opens the application in the default browser.

**Note:** When using the Docker driver on Windows, keep the terminal running this command open while accessing the application.

![Minikube service tunnel](screenshots/05-service-tunnel.png)

### Step 6: Verify the Nginx Web Page

The browser displays the default Nginx welcome page, confirming that the web server is accessible.

![Nginx welcome page](screenshots/06-nginx-browser.png)

### System Internal Details

What happens inside Kubernetes when `kubectl run hello-k8s --image=nginx --port=80` is executed:

1. **kubectl → kube-apiserver:** kubectl sends a Pod manifest (name `hello-k8s`, image `nginx`, port `80`) to the API server through its REST API.
2. **kube-apiserver → etcd:** the API server validates the request and stores the desired state in etcd: *there should be a Pod called `hello-k8s` running an nginx container on port 80*.
3. **kube-scheduler:** watches for new Pods that have no node assigned and chooses a worker node with enough CPU and memory.
4. **Scheduler → kubelet:** the Pod is bound to the chosen node, and the kubelet (the agent on that node) is told to run it.
5. **kubelet → container runtime:** the runtime pulls the `nginx` image from Docker Hub, creates the container, sets up its filesystem and runs it in isolated Linux namespaces.
6. **CNI (networking):** assigns the Pod a unique IP address that is reachable inside the cluster.
7. **kubelet → kube-apiserver:** the kubelet reports back that Pod `hello-k8s` is running, which is the status shown by `kubectl get pods`.

`kubectl expose` then creates a NodePort Service, and kube-proxy on the node routes traffic from the NodePort to the Pod.

## 6. Troubleshooting

**Issue: The Pod or Service already exists**

If Kubernetes reports that `hello-k8s` already exists, verify the existing resources:

```powershell
kubectl get pods
kubectl get services
```

If the resources are already running correctly, there is no need to recreate them.

**Issue: The application does not open**

- Check that the Pod status is `Running`.
- Verify that the Service exists.
- Run `minikube service hello-k8s` again if necessary.
- Keep the terminal running the Minikube service command open.

## 7. Key Concepts Learned

- **Minikube:** Runs a local Kubernetes cluster for development and learning.
- **Pod:** The smallest deployable unit in Kubernetes.
- **Container Image:** Nginx provides the web server application.
- **Service:** Provides a stable way to access a Pod.
- **NodePort:** Exposes a Service through a port on the Kubernetes node.
- **kubectl:** Command-line tool used to interact with Kubernetes.

## 8. Result

The Nginx application was successfully deployed as a Kubernetes Pod using Minikube. A NodePort Service was created, and the Nginx welcome page was accessed through a web browser.

## 9. Conclusion

This experiment demonstrated the basic Kubernetes deployment workflow, including starting a local cluster, deploying a containerized application, exposing it through a Service, and verifying application accessibility.