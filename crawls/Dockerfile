FROM ubuntu:14.04
MAINTAINER Khozzy <khozzy@gmail.com>

USER root

ENV CHROME_DRIVER_VERSION 2.14
ENV PYTHON_VERSION 2.7.10
ENV PYTHON_PIP_VERSION 7.0.3
ENV LANG C.UTF-8
ENV DISPLAY :99
ENV UID 1000
ENV GID 1000

ENV DIR /src/
RUN mkdir ${DIR}
COPY requirements.txt ${DIR}
WORKDIR ${DIR}

#================================================
# Add dedicated user
#================================================
RUN groupadd -r chrome -g $GID && useradd -u $UID -r -m -g chrome chrome

#================================================
# Customize sources for apt-get
#================================================
RUN  echo "deb http://archive.ubuntu.com/ubuntu trusty main universe\n" > /etc/apt/sources.list \
  && echo "deb http://archive.ubuntu.com/ubuntu trusty-updates main universe\n" >> /etc/apt/sources.list

RUN apt-get update -qqy \
  && apt-get -qqy install build-essential wget unzip curl xvfb xz-utils zlib1g-dev libssl-dev

#===============
# Google Chrome
#===============
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
  && echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list \
  && apt-get update -qqy \
  && apt-get -qqy install google-chrome-stable \
  && rm /etc/apt/sources.list.d/google-chrome.list \
  && rm -rf /var/lib/apt/lists/*

#==================
# Chrome webdriver
#==================

RUN wget --no-verbose -O /tmp/chromedriver_linux64.zip http://chromedriver.storage.googleapis.com/$CHROME_DRIVER_VERSION/chromedriver_linux64.zip \
  && rm -rf /opt/selenium/chromedriver \
  && unzip /tmp/chromedriver_linux64.zip -d /opt/selenium \
  && rm /tmp/chromedriver_linux64.zip \
  && mv /opt/selenium/chromedriver /opt/selenium/chromedriver-$CHROME_DRIVER_VERSION \
  && chmod 755 /opt/selenium/chromedriver-$CHROME_DRIVER_VERSION \
  && ln -fs /opt/selenium/chromedriver-$CHROME_DRIVER_VERSION /usr/bin/chromedriver

#==================
# Python
#==================
RUN apt-get install -y python python-pip python-dev libxml2-dev libxslt-dev libffi-dev libssl-dev

RUN ["pip","install","-r","requirements.txt"]
LABEL version="1.0" \
      description="This image is used for scarpy
#==================
# Xvfb + init scripts
#==================
ADD libs/xvfb_init /etc/init.d/xvfb
RUN chmod a+x /etc/init.d/xvfb

ADD libs/xvfb-daemon-run /usr/bin/xvfb-daemon-run
RUN chmod a+x /usr/bin/xvfb-daemon-run

#============================
# Clean up
#============================
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* ~/.config/google-chrome

USER chrome
