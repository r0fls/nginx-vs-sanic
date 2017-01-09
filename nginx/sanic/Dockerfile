FROM python:3.5
#RUN apt-get update
#RUN apt-get -y upgrade
#RUN apt-get -y install python3.5 python3-pip
#RUN apt-get -y install python3-dev
ADD ./ /home/
RUN pip3 install sanic
WORKDIR /home

CMD ["python3", "/home/hello.py"]
