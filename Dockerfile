FROM ubuntu:latest

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y python3
RUN apt-get install -y pip

WORKDIR /usr/src/app

#COPY requirements.txt ./
#RUN pip install --no-cache-dir -r requirements.txt
RUN pip install youtube-transcript-api
RUN pip install nltk
RUN pip install bs4

#install node
RUN apt-get install -y nodejs
RUN apt-get install -y npm

COPY . .

CMD ["bash", "-c", "while true; do sleep 3600; done"]
#CMD [ "python", "./summarize_yt_video_or_webpage/web_page_handler.py.py" ]