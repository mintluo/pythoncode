name_song = "Blowin' in the Wind"
name_singer = "Bob Dylan"
tail = "1962 by Warner Bros.Inc."

with open('Blow in the wind.txt','r+') as file:
    lyric = file.readlines()

lyric.insert(0,name_song+'\n')
lyric.insert(1,name_singer+'\n')
lyric.append('\n'+tail)

for line in lyric:
    print(line)

with open('Blow in the wind.txt','r+') as file:
    file.writelines(lyric)
    file.close()
