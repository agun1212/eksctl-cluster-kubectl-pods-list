# **Eksctl-cluster-kubectl-pods-list**


**AWS EKS Setup for Testing in Staging Server**

**Step1:** I have created Aws-EC2-instance to Setup Kubernetes on Amazon EKS 

**Step2:** You can follow same procedure in the official AWS document (https://docs.aws.amazon.com/eks/latest/userguide/getting-started-eksctl.html)

**Step3:** Setup the installation with kubectl && eksctl package download in EC2 instance 

**Step4:** Create an IAM Role and attache it to EC2 instance

**Step5:** Create your cluster and nodes with

**Step6:** Cluster name --region  --nodetype

**Step7:** Validate the cluster && node is created successfully.

**Step8:**  I have Created a pod with the

**Example:**  
**(podname) mytest-pod1 --image=bitnami/nginx:latest  --port=80 --labels=="app=team_system"**

Similarly, i have created 5 pods in the cluster node with different (podname) --image --port --lables

![image](https://user-images.githubusercontent.com/106250898/171938394-ccdcc35c-ce0f-43aa-8380-4f083ae86ef3.png)

Here I have written a python code to evaluates the current status of a all running pods in a cluster and evaluating some rules.

**rules:**
- name: image_prefix
  description: "ensure the pod only uses images prefixed with `bitnami/`"
  output: boolean
- name: team_label_present
  description: "ensure the pod contains a label `team` with some value"
  output: boolean
- name: recent_start_time
  description: "ensure the pod has not been running for more than 7 days according to its `startTime`"
  output: boolean
```

The service should evaluate these rules for all pods in the cluster, as well as output the results on stdout in json log format one line per pod.

The results on stdout should look like the following example:

```json
{"pod": "mytest", "rule_evaluation": [{"name": "image_prefix", "valid": true}, {"name": "team_label_present", "valid": true}, {"name": "recent_start_time", "valid": false}]}
{"pod": "another", "rule_evaluation": [{"name": "image_prefix", "valid": false}, {"name": "team_label_present", "valid": true}, {"name": "recent_start_time", "valid": false}]}


For this Kubernetes Pod Evaluation Service

We need an output file from each eks cluster nodes by running the below command.

Kubectl get pods -o=jsonpath='{range .items[*]}{.metadata.name}{";"}
{.metadata.labels}{";"}{.status.startTime}{";"}{.status.phase}{";"}{range .spec.containers[*]}{.image}{"\n"}{end}' > latest-output.txt


**Output:**

![image](https://user-images.githubusercontent.com/106250898/171945964-d0eb53a0-ac6b-40b3-b941-6c353e10a1f1.png)



**How to Run this Code to set & filter with some rules**
====================================================================================================================

Call the output file as a input inside the pyton script to evalute the current status of a all pods in a cluster with evaluating the mentioned some rules.

To run the script we need the updated python 3.6 (or) python 3.7 

Place the 2 files inside the same Directory to avoid error
**File1:**  **latest-ouput.txt **
**File2:**  **pod-filter-list.py**

Finally Run the script with the commad : **python3 pod-filter-list.py**

** Here the stdout Json log format output:**

![image](https://user-images.githubusercontent.com/106250898/171948772-e19ddccf-7a17-4fd3-ab51-6b3da8915099.png)



