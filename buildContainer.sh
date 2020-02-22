sudo docker rmi $(sudo docker images | grep 'ubuntu_test')
sudo docker build --no-cache -t ubuntu_test .
