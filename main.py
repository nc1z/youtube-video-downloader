from pytube import YouTube

def download_youtube_video(url):
    try:
        yt = YouTube(url)
        video = yt.streams.get_highest_resolution()
        video.download()
        print("Download completed!")
    except Exception as e:
        print("Error:", str(e))

video_url = str(input("Enter youtube video URL: "))
download_youtube_video(video_url)
