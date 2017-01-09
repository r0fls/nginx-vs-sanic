FROM python:3.5
RUN apt-get install git
RUN git clone https://github.com/r0fls/sanic /home/sanic
WORKDIR /home/sanic
RUN pip3 install -r /home/sanic/requirements.txt
RUN git checkout vhosts
ADD ./ /home/sanic

CMD ["python3", "/home/sanic/hello.py"]
