from youtube_transcript_api import YouTubeTranscriptApi



def get_video_id(url_link):
  if "/shorts/" in url_link:
     return url_link.split("/shorts/")[-1]
  return url_link.split("watch?v=")[-1]

def get_youtube_text(video_link):
    transcript = YouTubeTranscriptApi.get_transcript(get_video_id(video_link))
    transcript_joined = ' '.join([line['text'] for line in transcript])
    return transcript_joined

text = get_youtube_text('https://www.youtube.com/shorts/BI2OumGAhNI')
print(text)


#TODO: create sentencies from generated youtube subtitle +summarize

