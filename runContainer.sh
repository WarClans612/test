sudo docker rm $(sudo docker stop $(sudo docker ps -a -q --filter="name=ubuntu_test"))
sudo docker run -it -d -v /home/phua/Lab_Project/test:/test -p 12345:22 -p 12346:21  --name ubuntu_test ubuntu_test:latest
	
