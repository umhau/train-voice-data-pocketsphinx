import thread, time
import pyaudio
import wave
import sys

chunk = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

# create interrupt thread
def input_thread(L):
    raw_input()
    L.append(None)


def do_recording(WAVE_OUTPUT_FILENAME):

    # initialize audio stream
    p = pyaudio.PyAudio()
    stream = p.open(format = FORMAT,
            channels = CHANNELS,
            rate = RATE,
            input = True,
            frames_per_buffer = chunk)

    L = []
    thread.start_new_thread(input_thread, (L,))
    audio_recording = []
    print "recording"
    
    while 1:
        # record data during loop
        data = stream.read(chunk)
        audio_recording.append(data)
        if L: break
    
    # exit cleanly after break
    stream.close()
    p.terminate()
    
    # write data to WAVE file
    data = ''.join(audio_recording)
    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(data)
    wf.close()




# look for 'bespoke_training_data' folder, if missing create

# if exists, see how far the recording process went

# get file

# get lines from file

# display line, record until interrupt












for x in range(2):
    raw_input("ready for next input?")
    do_recording("test.1.wav")










