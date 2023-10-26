FROM apache/nifi:latest



USER root

COPY ./script /opt/nifi/scripts

RUN apt-get update && apt-get install -y python3.11 python3-pip
# Install libraries
RUN pip3 install pandas
RUN pip3 install datetime
RUN pip3 install openpyxl
RUN pip3 install convertdate
RUN pip3 install numpy
RUN pip3 install excel