# Choosing the image.
FROM python:3.10-slim

#Updating and installing 'alien'.
RUN apt-get update -y && apt-get install alien -y

# copy requirements.txt
COPY  requirements.txt /app/

WORKDIR /app


# downloading oracle drivers.
ADD https://download.oracle.com/otn_software/linux/instantclient/195000/oracle-instantclient19.5-basiclite-19.5.0.0.0-1.x86_64.rpm ./instantclient19.5-basiclite.rpm

# converting the file to .deb format and thereafter removing the installation files.
RUN alien -i  --scripts  ./instantclient19.5-basiclite.rpm && rm ./instantclient19.5-basiclite.*

# Installing the app requirements.
RUN pip install -r requirements.txt && apt-get install libaio1 libaio-dev -y && apt-get remove alien -y

# setting up the env variables.
ENV LD_LIBRARY_PATH="/usr/lib/oracle/19.5/client(64)/lib/${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}"
ENV ORACLE_HOME="/usr/lib/oracle/19.5/client(64)"
ENV PATH="/usr/lib/oracle/19.5/;"+${PATH}


COPY . /app


CMD python mainProject.py