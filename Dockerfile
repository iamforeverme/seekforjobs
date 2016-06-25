FROM django:1.9.5-python2
MAINTAINER Kevin
ENV DIR /src/
RUN mkdir ${DIR}
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 627220E7
RUN echo 'deb http://archive.scrapy.org/ubuntu scrapy main' | tee /etc/apt/sources.list.d/scrapy.list
RUN apt-get update && apt-get install -y libxml2-dev libxslt1-dev zlib1g-dev libffi-dev libssl-dev fontconfig supervisor bzip2 curl
RUN curl -sL https://deb.nodesource.com/setup | bash -
RUN apt-get install -y nodejs #npm
RUN npm -g install phantomjs
#VOLUME . ${DIR}
COPY requirements.txt .
RUN ["pip","install","-r","requirements.txt"]
WORKDIR ${DIR}
LABEL version="1.0" \
      description="This image is used to set up django sevier."
