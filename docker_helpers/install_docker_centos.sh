script_dir=$(dirname $0)
sudo sh $script_dir/remove_docker_centos.sh

# create folders in $HOME for docker and containerd
sudo mkdir /home/docker_stuff
sudo mkdir /home/docker_stuff/docker
sudo mkdir /home/docker_stuff/containerd
sudo ln -s /home/docker_stuff/docker /var/lib/docker
sudo ln -s /home/docker_stuff/containerd /var/lib/containerd

sudo yum install -y yum-utils

sudo yum-config-manager \
    --add-repo \
    https://download.docker.com/linux/centos/docker-ce.repo

sudo yum install docker-ce docker-ce-cli containerd.io
sudo systemctl start docker
