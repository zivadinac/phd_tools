script_dir=$(dirname $0)
sudo sh $script_dir/remove_docker_ubuntu.sh

# create folders in /home for docker and containerd
sudo mkdir /home/docker_stuff
sudo mkdir /home/docker_stuff/docker
sudo mkdir /home/docker_stuff/containerd
sudo ln -s /home/docker_stuff/docker /var/lib/docker
sudo ln -s /home/docker_stuff/containerd /var/lib/containerd

sudo apt-get update

sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg \
    lsb-release

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

echo \
  "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io
