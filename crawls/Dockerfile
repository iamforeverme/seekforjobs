FROM vimagick/scrapyd:latest
MAINTAINER Kevin
ENV DIR /src/
RUN mkdir ${DIR}
COPY requirements.txt ${DIR}
WORKDIR ${DIR}
RUN ["pip","install","-r","requirements.txt"]
LABEL version="1.0" \
      description="This image is used for scarpy."