import pytube

link=input('Enter link:')
yt=pytube.Youtube(link)
yt.streams.first().download()
print('Downloaded', link)