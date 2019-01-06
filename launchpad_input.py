import os
from pydub import AudioSegment
from pydub.playback import play

#看你的音檔位置在哪裡，然後指定位置
os.chdir('D://USER//desktop//')
#設定變數名稱，不同種類的音檔就用from_XXX   XXX=mp3,WAV,ogg......etc
song = AudioSegment.from_mp3("劉宇祥－米津玄師－Lemon剪輯 by AF.mp3")
#播放
play(song)