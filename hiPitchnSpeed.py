from pydub import AudioSegment

def hiPitchnSpeed(sound, level):

    # 每次升高半音
    octaves = 0.5
    new_rate = int(sound.frame_rate * (level ** octaves))

    hipitch_sound = sound._spawn(sound.raw_data, overrides={'frame_rate': new_rate})
    hipitch_sound = hipitch_sound.set_frame_rate(44100)
	
    return hipitch_sound

	
audioInput = AudioSegment.from_file("D:\\college\\107-1\\商管程式設計\\Final_Project\\sample1.wav", format="wav")
audioOuput = hiPitchnSpeed(audioInput, 6)
audioOuput.export("D:\\college\\107-1\\商管程式設計\\Final_Project\\hiPitchnSpeed.wav", format="wav")

'''同時提高音頻和速率'''