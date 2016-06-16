FROM django:1.9.5-python2
MAINTAINER Kevin
ENV DIR /src/
RUN mkdir ${DIR}
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 627220E7
RUN echo 'deb http://archive.scrapy.org/ubuntu scrapy main' | tee /etc/apt/sources.list.d/scrapy.list
RUN apt-get update && apt-get install -y libxml2-dev libxslt1-dev zlib1g-dev libffi-dev libssl-dev fontconfig supervisor bzip2
#VOLUME . ${DIR}
COPY requirements.txt .
RUN ["pip","install","-r","requirements.txt"]
ENV PHANTOMJS_REMOTE https://npm.taobao.org/mirrors/phantomjs/phantomjs-2.1.1-linux-x86_64.tar.bz2
ENV PHANTOMJS phantomjs-2.1.1-linux-x86_64.tar.bz2
#RUN wget --no-check-certificate -b -o $PHANTOMJS $PHANTOMJS_REMOTE
COPY $PHANTOMJS .
RUN ls -al $PHANTOMJS
RUN tar -jxvf $PHANTOMJS
RUN chmod a+x /phantomjs-2.1.1-linux-x86_64/bin/phantomjs
RUN ln -sf /phantomjs-2.1.1-linux-x86_64/bin/phantomjs /usr/bin/phantomjs
WORKDIR ${DIR}
LABEL version="1.0" \
      description="This image is used to set up django sevier."
