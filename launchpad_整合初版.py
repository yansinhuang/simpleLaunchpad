import os
import tkinter as tk
import tkinter.font as tkFont
import tkinter.filedialog as fdl
from aupyom import Sampler, Sound
from ipywidgets import interact, FloatSlider
from pydub import AudioSegment
from pydub.playback import play
from threading import Thread

# 看你的音檔位置在哪裡，然後指定位置
os.chdir('D://USER//desktop//')
#設定變數名稱，不同種類的音檔就用from_XXX   XXX=mp3,WAV,ogg......etc


class lunchfunc():
	# 調整頻率和速率的函數
	def soundModifier(pitch, stretch):
		s1.pitch_shift = pitch
		s1.stretch_factor = stretch

	'''
	以下五個函數做成按鈕
	'''
	# 頻率上升，原速率
	def pitchUp(self):
		soundModifier(1, 1)

	# 頻率下降，原速率
	def pitchDn(self):
		soundModifier(-1, 1)

	# 回到原頻率原速率
	def resetBoth(self):
		soundModifier(0, 1)

	# 原頻率，速率上升
	def speedUp(self):
		soundModifier(0, 2)

	# 原頻率，速率下降
	def speedDn(self):
		soundModifier(0, 0.5)
	
	def stop():
		sampler.remove(s1)	

#song_name = 'Lucid_Dreamer.mp3'
class launchpad(tk.Frame):

	def __init__(self):
		tk.Frame.__init__(self)
		self.grid()
		self.createwidgets()

    # 多線程
	def threaded_run_0(self, event):
		t = Thread(target=self.song0_start)
		t.daemon = True
		t.start()
	def threaded_run_1(self, event):
		t = Thread(target=self.song1_start)
		t.daemon = True
		t.start()
	def threaded_run_2(self, event):
		t = Thread(target=self.song2_start)
		t.daemon = True
		t.start()
	def threaded_run_3(self, event):
		t = Thread(target=self.song3_start)
		t.daemon = True
		t.start()

    # 視窗
	def createwidgets(self):
	# 字型
		f1 = tkFont.Font(size=20, family='Ink Free')
		# 三個按鍵
		self.btnnum0 = tk.Button(self, text='choose',height=1, width=20, command=self.choose_song, font=f1)
		self.btnnum1 = tk.Button(self, text='vocal', height=1, width=10, command=self.threaded_run_1, font=f1)
		self.btnnum2 = tk.Button(self, text='drum', height=1, width=10, command=self.threaded_run_2, font=f1)
		self.btnnum3 = tk.Button(self, text='guitar', height=1, width=10, command=self.threaded_run_3, font=f1)
		self.btnnum0_1 = tk.Button(self, text='',height=1, width=10, command=self.threaded_run_0, font=f1)
		# 按鍵排版
		self.btnnum0.grid(row=0, column=0, sticky=tk.NE + tk.SW)
		self.btnnum1.grid(row=1, column=0, sticky=tk.NE + tk.SW)
		self.btnnum2.grid(row=2, column=0, sticky=tk.NE + tk.SW)
		self.btnnum3.grid(row=3, column=0, sticky=tk.NE + tk.SW)
		self.btnnum0_1.grid(row=0, column=1, sticky=tk.NE + tk.SW)
		# 鍵盤操作
		self.btnnum0.bind_all('q', self.threaded_run_0)
		self.btnnum1.bind_all('a', self.threaded_run_1)
		self.btnnum2.bind_all('s', self.threaded_run_2)
		self.btnnum3.bind_all('d', self.threaded_run_3)
		
	def choose_song(self):
		default_dir = r"D://USER//desktop"  # 设置默认打开目录
		global song_name
		song_name = fdl.askopenfilename(title=u"选择文件", initialdir=(os.path.expanduser(default_dir)))
		
	
	def song0_start(self):
		sampler = Sampler()
		s1 = Sound.from_file(song_name)
		lunchfunc.pitchUp(s1)
		sampler.play(s1)	
	
	def song1_start(self):
		play(song1)


	def song2_start(self):
		play(song2)


	def song3_start(self):
		play(song3)
		
	
	# 回到原頻率原速率
	def resetBoth(self, sound):
		sound.pitch_shift = 0
		sound.stretch_factor = 1

	# 頻率上升，原速率
	def pitchUp(self, sound):
		sound.pitch_shift = 1

	# 頻率下降，原速率
	def pitchDn(self, sound):
		sound.pitch_shift = -1
		
	# 原頻率，速率上升
	def speedUp(self, sound):
		sound.stretch_factor = 2
		
	# 原頻率，速率下降
	def speedDn(self, sound):
		sound.stretch_factor = 0.5
		
	def stop(self, sound):
		sampler.remove(sound)



song2 = AudioSegment.from_mp3("Japanese_drum1.mp3")
song3 = AudioSegment.from_mp3("guitar.mp3")
# 播放



# 運作
window = launchpad()
window.master.title('launchpad')
window.mainloop()

