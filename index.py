from pytube import YouTube
format = 'mp4'
YouTube('https://youtu.be/9bZkp7q19f0').streams.first().download(filename=f'GANG.{format}')
yt = YouTube('https://youtu.be/9bZkp7q19f0')
yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(filename= f'STYLE.{format}')
