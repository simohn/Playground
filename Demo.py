import vlc

# url = 'http://mp3stream1.apasf.apa.at:8000'
url = 'http://mp3stream7.apasf.apa.at:8000'
instance = vlc.Instance()
player = instance.media_player_new()
media = instance.media_new(url)
media.get_mrl()
player.set_media(media)

player.play()
