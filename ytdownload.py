from pytube import YouTube 

link = input("YouTube URL: ")
yt = YouTube(link)
videos = yt.streams.all()

video = list(enumerate(videos))

for i in video:
    print(i)

    