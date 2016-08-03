# train-voice-data-pocketsphinx

last modified 8.3.2016 by umhau

A script to automate training voice data for PocketSphinx.  The only file you need is train_voice_model.py.  Put this in the directory where you want your training data folder to be located.  It will look for a folder called 'bespoke_training_data' and create it if necessary.  Then you just have to sit there and read the text it feeds you on the screen. There's 500+ sentences to read, but you only really need about 20.  I'd go for more.  

You can pick up later if you need to; the script will look for the highest numbered file and start recording after that.  I haven't tested what happens when it reaches the end of the list.  Hopefully the exit is clean. 
