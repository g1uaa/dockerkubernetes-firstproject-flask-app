# Your docker image is based off a base image, in this case
# Base python docker image -- get from docker hub website as:
 FROM python:3.9.7-buster

#Import code -- from current dir into /code dir
 ADD . /code

# changing the dir
 WORKDIR /code

#Installing pkg and libs (dependency)
 RUN pip install flask

# Exposing the port
 EXPOSE 5001

# Running your pyton module/file as
 CMD python app.py