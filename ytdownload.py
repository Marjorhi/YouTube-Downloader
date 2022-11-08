from pytube import YouTube 

link = input("YouTube URL: ")
yt = YouTube(link)
videos = yt.streams.all()

video = list(enumerate(videos))

for i in video:
    print(i)

    print("Enter the option to download the format: ")
    dn_option = int(input("Enter the option: "))

    dn_video = videos[dn_option]
    dn_video.download()

    print("Downloaded successfully")