# quick script to make a test recording usable by PocketSphinx.



import pyaudio
import wave
 
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
CHUNK = 1024
RECORD_SECONDS = 5

def dinput(prompt,default_input):
    # unsophisticated function that lets you have a default input.
    # does not perform checks on the input.
    r_in = raw_input(prompt + ' [%s]' % str(default_input))
    i = str(r_in) or default_input
    return i


WAVE_OUTPUT_FILENAME = dinput("Enter the full filename you want to use. ", "./test-file.wav")

raw_input("You will have 5 seconds to record your arbitrary test sequence. Press [enter] when ready.")

audio = pyaudio.PyAudio()
 
# start Recording
stream = audio.open(format=FORMAT, channels=CHANNELS,
                rate=RATE, input=True,
                frames_per_buffer=CHUNK)
print "recording..."
frames = []
 
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)
print "finished recording"
 
 
# stop Recording
stream.stop_stream()
stream.close()
audio.terminate()
 
waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
waveFile.setnchannels(CHANNELS)
waveFile.setsampwidth(audio.get_sample_size(FORMAT))
waveFile.setframerate(RATE)
waveFile.writeframes(b''.join(frames))
waveFile.close()







    