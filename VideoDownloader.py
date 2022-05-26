import os

# Path o the yt-dlp.exe
# You can also use the full path to your yt-dlp.exe in the "Python\Python39\Scripts\yt-dlp.exe" folder
yt_dlp = r'yt-dlp.exe '
# Path of the Youtube file
Youtube = 'Youtube.txt'
# Path of the Main Folder  
savePath ='D:\Libraries'

# Options are strings based 
#  0         for default
#  ml,ML     for audio only lists
#  l,L,list  for list 
#  v,V,Video for video 
#  m,M,music for audio only


file = open(Youtube, "r")
error   = 0
for line in file:
    call = yt_dlp                   # The yt_dlp Command
    line = line.split(',')          # Split URL,Folder,Option

    try:                            # Check Folder Field
        folder = line[1]
    except:                         # Set Default Folder
        folder = ''  

    try:                            # Check Option Field
        option = line[2]
    except:                         # Set Default Option
        option = 'v'

    code = line[0] 
    audio = {'m','M','music','ml','ML'}
    video = {'v','V','video'}
    list = {'l','L','list'}

    if option in audio:
        call += '-x --audio-format mp3 --audio-quality 0 '
        call += '--embed-metadata '
        call += '--postprocessor-args "-metadata album={} -metadata album_artist={} -metadata track=" '.format(folder,folder)
        call += '-o "{}\Music\{}\%(title)s.%(ext)s" '.format(savePath, folder)
        
    if option in list:
        call += '--playlist-start 1 '
        call += '-o "{}\List\{}\%(playlist_index)s - %(title)s.%(ext)s" '.format(savePath, folder)  

    if option in video:
        call += '-o "{}\Video\{}\%(title)s.%(ext)s" '.format(savePath, folder)

    call += code
    os.system(call)

file.close()

# CLEAR THE FILE
if error == 0:
    w = open(Youtube, "w")
    w.close()
    
