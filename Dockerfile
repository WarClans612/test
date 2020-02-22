FROM ubuntu:18.04

RUN apt-get update -y
RUN apt-get install -y openssh-server

CMD ["echo", "something"]
CMD ["/bin/bash"]

