FROM vimagick/scrapyd:latest
MAINTAINER Kevin
ENV DIR /src/
RUN mkdir ${DIR}
COPY requirements.txt ${DIR}
WORKDIR ${DIR}
RUN ["pip","install","-r","requirements.txt"]
# Install Chromium and ChromeDriver
#RUN echo -e "\ndeb http://downloads.sourceforge.net/project/ubuntuzilla/mozilla/apt all main" | tee -a /etc/apt/sources.list > /dev/null

#RUN echo -e "\ndeb http://downloads.sourceforge.net/project/ubuntuzilla/mozilla/apt all main" | tee -a /etc/apt/sources.list > /dev/null
#RUN apt-key adv --recv-keys --keyserver keyserver.ubuntu.com C1289A29
#RUN echo "\ndeb http://mozilla.debian.net/ jessie-backports firefox-release " >> /etc/apt/sources.list
#RUN apt-get update
#RUN apt-get install -y --force-yes -t jessie-backports firefox
#RUN apt-get install -y iceweasel-l10n-zh-cn
# Install Chrome
RUN echo 'deb http://httpredir.debian.org/debian testing main' >> /etc/apt/sources.list && \
	apt-get update && apt-get install -y \
	ca-certificates \
	curl \
	hicolor-icon-theme \
	libgl1-mesa-dri \
	libgl1-mesa-glx \
	libv4l-0 \
	-t testing \
	fonts-symbola \
	--no-install-recommends \
	&& curl -sSL https://dl.google.com/linux/linux_signing_key.pub | apt-key add - \
	&& echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google.list \
	&& apt-get update && apt-get install -y \
	google-chrome-stable \
	--no-install-recommends

# Install Chrome WebDriver
RUN wget --no-verbose -O /tmp/chromedriver_linux64.zip http://chromedriver.storage.googleapis.com/2.10/chromedriver_linux64.zip
RUN mkdir -p /opt/chromedriver-2.10
RUN apt-get update -qq && DEBIAN_FRONTEND=noninteractive apt-get install -yqq\
    unzip
RUN unzip /tmp/chromedriver_linux64.zip -d /opt/chromedriver-2.10
RUN chmod +x /opt/chromedriver-2.10/chromedriver
RUN rm /tmp/chromedriver_linux64.zip
RUN ln -fs /opt/chromedriver-2.10/chromedriver /usr/local/bin/chromedriver
LABEL version="1.0" \
      description="This image is used for scarpy."