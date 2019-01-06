import wave

CHANNELS = 1
swidth = 2
Change_RATE = 6

# 輸入音檔之路徑
spf = wave.open('D:\\college\\107-1\\商管程式設計\\Final_Project\\sample1.wav', 'rb')
RATE = spf.getframerate()
signal = spf.readframes(-1)

# 輸出音檔之位置
wf = wave.open('D:\\college\\107-1\\商管程式設計\\Final_Project\\speedup6.wav', 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(swidth)
wf.setframerate(RATE * Change_RATE)
wf.writeframes(signal)
wf.close()

'''加速音檔，但會改變頻率'''