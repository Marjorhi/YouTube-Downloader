from pytube import YouTube 

link = input("YouTube URL: ")
yt = YouTube(link)
videos = yt.streams.all()

