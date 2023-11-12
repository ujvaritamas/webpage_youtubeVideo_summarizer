# webpage_youtubeVideo_summarizer
Summarize webpage or youtube video with basic NLP

TODO: youtube_handler not finished yet.
TODO: make the code cleaner


Additional Info

cd workdir
Create image:
docker build -t wp_yt_summary_img .

debug:

docker run -d --name test -v $(pwd)/summarize_yt_video_or_webpage:/myapp wp_yt_summary_img

docker run -d --name test -v $(pwd)/summarize_yt_video_or_webpage:/myapp -p 8080:80 wp_yt_summary_img

docker exec -it <containerid> /bin/bash

cleanup:

#delete docker : docker image prune -a, docker image prune -a, docker system prune --volumes