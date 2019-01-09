from aupyom import Sampler, Sound
from ipywidgets import interact, FloatSlider
'''	
aupyom可以去這裡clone 
https://github.com/pierre-rouanet/aupyom.git
或是在命令列用git或pip install
ipywidgets也是 
'''

sampler = Sampler()

# 調整頻率和速率的函數
def soundModifier(pitch, stretch):
	s1.pitch_shift = pitch
	s1.stretch_factor = stretch

'''
以下五個函數做成按鈕
'''
# 頻率上升，原速率
def pitchUp():
	soundModifier(1, 1)

# 頻率下降，原速率
def pitchDn():
	soundModifier(-1, 1)

# 回到原頻率原速率
def resetBoth():
	soundModifier(0, 1)

# 原頻率，速率上升
def speedUp():
	soundModifier(0, 2)

# 原頻率，速率下降
def speedDn():
	soundModifier(0, 0.5)
	
# 停止播放
def stop():
	sampler.remove(s1)

s1 = Sound.from_file("D:\\music\\Bon Jovi\\Bounce\\It's my Life.mp3")
sampler.play(s1)	

# 讓我們可以在音樂進行中改變參數，可在命令列輸入函數試試看
interact(soundModifier,
         pitch=FloatSlider(min=-10, max=10, value=0, step=0.5),
         stretch=FloatSlider(min=0.1, max=10, value=1.0, step=0.1));
		 
