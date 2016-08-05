# written by umhau August 2016
#
# note: use this link for nice output: http://stackoverflow.com/questions/517127/how-do-i-write-output-in-same-place-on-the-console

# INITIALIZE

print("--------------------------------------------------------------------------------")


import thread, time
import pyaudio
import wave
import sys
import string
import os
import errno
import re
import urllib2  # the lib that handles the url stuff
import glob

# these settings are crucial to making sure PocketSphinx works properly.
chunk = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000 

def dinput(prompt,default_input):
    # unsophisticated function that lets you have a default input.
    # does not perform checks on the input.
    r_in = raw_input(prompt + ' [%s]' % str(default_input))
    i = str(r_in) or default_input
    return i

# create interrupt thread.  This lets me record for an unspecified amount of time.
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

# it's nice to clear the screen easily.
def clear_screen():
    sys.stderr.write("\x1b[2J\x1b[H")


def get_name_of_training_data():
    wrong = True
    while wrong:
        training_data_name = dinput("What do you want to call this training data? ", "test-data")
        if ' ' in training_data_name:
            wrong = True
        else:
            wrong = False
    return training_data_name


def make_sure_path_exists(path):
    print("Looking for "+ training_data_name + " folder...")
    nf = []
    try:
        os.makedirs(path)
        print("Creating new folder for test data...")
        nf = True # did I create a new folder?
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise
    
    return nf


# if exists, see how far the recording process went

def how_much_training_data_exists_already(nf):
    
    path = "./" + training_data_name
    
    if not nf: # don't need to look stupid
        print("Checking for previous recordings...")
    
    file_list = glob.glob(path+'/*.wav')
    numbers_list = []
    
    for i in file_list:
        # print i # this would print the names of all .wav files (unneccessary)
        numbers_list.append(re.findall(".*" + training_data_name + "(\d+)\.wav", i))
    #print numbers_list
    try:
        #print max(numbers_list)
        number = int(max(numbers_list)[0])
    except ValueError:
        number = 0
    except IndexError:
        number = -1
    
    if number:
        if number == 0:
            print("Found 0 recordings.")
        elif number == -1:
            print("Found other files in directory.")
        elif number == 1:
            print("Found 1 recording.")
        else:
            print("Found %d recordings." % number)
    
    return number
    

def get_cmu_arctic_training_data_file():

    target_url = 'http://festvox.org/cmu_arctic/cmuarctic.data'
    print("Downloading dictation list...")
    data = urllib2.urlopen(target_url) 
    
    datalist = []
    
    for line in data: 
        try:
            # using the b-set of arctic data for testing purposes. Change this if I want to create 
            # more training data.
            matches = re.findall('\(\sarctic_b(?P<number>\d\d\d\d)\s\"(?P<text>.+)"\s\)', line, re.DOTALL)
            if matches:
                datalist.append(matches)
        except AttributeError:
            pass
        # print(matches)
    print("%d possible recordings." % len(datalist))
    # print datalist
    return datalist
    #print datalist


# print("--------------------------------------------------------------------------------")

def how_many_recordings(datalist):
    
    need = True # need a sensible number.
    while need:
        num_recs = raw_input("Number of recordings to make (total): ")
        try:
            if int(num_recs) > len(datalist):
                print("Please enter a smaller number.")
            elif int(num_recs) <= len(datalist):
                need = False
            
        except ValueError:
            print("Please enter an integer.")
    return int(num_recs)
    
 

def append_to_text_file(formatted_text, filename):
    hs = open(filename,"a")
    hs.write(formatted_text)
    hs.close() 
    
              
# display line, record until interrupt
def record_new_cmu_training_data(quant, num_recs, datalist):
    #clear_screen()
    print("\nRemember: read carefully.  Press [enter] to start when you are in a quiet area.  If you are not ready, or to leave at any time during recording, press [ctrl-c] to exit the script.  The script will pick up where it left off.\n")
    ready = raw_input()
    
    try:
        for i in datalist[quant:num_recs]: # iterate through data, starting after the last recording detected.
        
        # record audio
            if i==quant:
                delete = raw_input("Do you want to delete the last recording? (yes/no) ")
                if delete == 'yes':
                    print("Run delete_last_record.py from the command line.")
                    break

            clear_screen()
            print("Recording no. %s of %04d\n" % (i[0][0], num_recs))
            print("Read the following text out loud after pressing [enter]:")
            print("--------------------------------------------------------------------------------\n")
            print(i[0][1] + "\n")
            print("--------------------------------------------------------------------------------\n")
            

            
            # recording file should look like this (e.g.): ./bespoke_training_data/arctic1.wav
            audio_file_name = "./" + training_data_name + "/" + training_data_name + str(int(i[0][0])) + ".wav"
                              
            do_recording(audio_file_name)
            
        # add formatted data to language model files
        
        #transcription file
            nice_text = i[0][1].lower().translate(string.maketrans('', ''), ',.') 
            # format: some text (test1)
            formatted_txt = nice_text +  " (" + training_data_name + str(int(i[0][0])) + ")\n"
            # formatted_txt = "<s> " +  nice_text +  " </s> (" + training_data_name + "_" + str(i[0][0]) + ")\n"
            formatted_filename = "./" + training_data_name + "/" +training_data_name + '.transcription'             
            append_to_text_file(formatted_txt,formatted_filename)
        #fileid
            formatted_txt = training_data_name + str(int(i[0][0])) + "\n"
            # formatted_txt = training_data_name + "_" + str(i[0][0]) + "\n"
            formatted_filename = "./" + training_data_name + "/" +training_data_name + '.fileids'
            append_to_text_file(formatted_txt,formatted_filename)
                       
    except KeyboardInterrupt:
        sys.exit()
        
# functions

clear_screen()

training_data_name = get_name_of_training_data()

nf = make_sure_path_exists("./" + training_data_name)

datalist = get_cmu_arctic_training_data_file()

quant = how_much_training_data_exists_already(nf)

num_recs = how_many_recordings(datalist)

record_new_cmu_training_data(quant, num_recs, datalist)

print("Done.\n")

















