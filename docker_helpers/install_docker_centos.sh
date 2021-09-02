sh remove_docker_centos.sh

# create folders in $HOME for docker and containerd
mkdir ~/docker_stuff
mkdir ~/docker_stuff/docker
mkdir ~/docker_stuff/containerd
ln -s ~/docker_stuff/docker /var/lib/docker
ln -s ~/docker_stuff/containerd /var/lib/containerd

yum install -y yum-utils

yum-config-manager \
    --add-repo \
    https://download.docker.com/linux/centos/docker-ce.repo

yum install docker-ce docker-ce-cli containerd.io
systemctl start docker
