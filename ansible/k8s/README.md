## k8s-ansible
Simple kubernetes cluster setup ansible script, which install all the dependencies on master and worker nodes with flannel CNI, and init the cluster.

# How to connect workers to the cluster?

If you want to connect workers to the cluster, you need to copy out the kubeadm join command, that's it.


Tested on:
Ubuntu 22.04 LTS - K8s version: v1.26.0