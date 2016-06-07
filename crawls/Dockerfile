FROM vimagick/scrapyd:latest
MAINTAINER Kevin
ENV DIR /src/
ENV PHANTOMJS_REMOTE https://npm.taobao.org/mirrors/phantomjs/phantomjs-2.1.1-linux-x86_64.tar.bz2
ENV PHANTOMJS phantomjs-2.1.1-linux-x86_64.tar.bz2
RUN mkdir ${DIR}
RUN echo 'deb http://mirrors.ustc.edu.cn/debian jessie main contrib non-free\ndeb-src http://mirrors.ustc.edu.cn/debian jessie main contrib non-free\ndeb http://mirrors.ustc.edu.cn/debian jessie-proposed-updates main contrib non-free\ndeb-src http://mirrors.ustc.edu.cn/debian jessie-proposed-updates main contrib non-free\ndeb http://mirrors.ustc.edu.cn/debian jessie-updates main contrib non-free\ndeb-src http://mirrors.ustc.edu.cn/debian jessie-updates main contrib non-free' > /etc/apt/sources.list
RUN apt-get update
RUN apt-get install -y bzip2
#RUN apt-get install -y wget
#RUN rm -f $PHANTOMJS
#RUN wget --no-check-certificate -b -o $PHANTOMJS $PHANTOMJS_REMOTE
#RUN ls -al phantomjs-2.1.1-linux-x86_64.tar.bz2
RUN rm -rf $PHANTOMJS
COPY $PHANTOMJS .
RUN ls -al $PHANTOMJS
RUN tar -jxvf $PHANTOMJS
RUN ln -sf /phantomjs-2.1.1-linux-x86_64/bin/phantomjs /usr/bin/phantomjs
RUN apt-get install -y fontconfig
COPY requirements.txt ${DIR}
WORKDIR ${DIR}
RUN ["pip","install","-r","requirements.txt"]
RUN wget
LABEL version="1.0" \
      description="This image is used for scarpy."