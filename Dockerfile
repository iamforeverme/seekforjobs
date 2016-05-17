FROM django:1.9.5-python3
MAINTAINER Kevin
ENV DIR /src/
RUN mkdir ${DIR}
#VOLUME . ${DIR}
COPY requirements.txt ${DIR}
WORKDIR ${DIR}
RUN ["pip","install","-r","requirements.txt"]
LABEL version="1.0" \
      description="This image is used to set up django sevier."