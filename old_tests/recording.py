print "* record until keypress"
from openexp.keyboard import keyboard
# Short timeout so get_key() doesn't block
my_keyboard = keyboard(exp, timeout=2)
all = []
while my_keyboard.get_key()[0] == None: # Loop until a key has been pressed
    data = stream.read(chunk) # Record data
    all.append(data) # Add the data to a buffer (a list of chunks)
print "* done recording"
