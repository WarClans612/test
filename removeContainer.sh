sudo docker rm $(sudo docker stop $(sudo docker ps -a -q --filter="name=ubuntu_test"))
