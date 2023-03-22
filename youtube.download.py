from pytube import YouTube

# initialize the YouTube object
yt = YouTube('https://youtu.be/-OFyb34InYU')

# print some basic information about the video
print(f'Title: {yt.title}')
print(f'Duration: {yt.length} seconds')
print(f'Views: {yt.views}')

# select the highest quality video and download it
ys = yt.streams.get_highest_resolution()
ys.download('/home/ted/Desktop/int/4.2/project/datasets')
