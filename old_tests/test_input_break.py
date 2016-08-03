input = raw_input("Test version 1, 2, or 3?")
if input=='1':
    import pygame, sys
    from pygame.locals import *
    
    pygame.init()
    pygame.display.set_mode((100,100))
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT: sys.exit()
            if event.type == KEYDOWN and event.dict['key'] == 50:
                print 'break'
    pygame.event.pump()

if input=='2':
    try:
        while 1:
            # do loop stuff
            print("|")
            print("\b/")
            print("\b--")
            print("\b\\")
            print("\b|")
            print("\b/")
            print("\b--")
            print("\b\\")
            print("\b")
    except KeyboardInterrupt: # problem is, that's a CTRL-C
        # do post-loop stuff
        print("you interupted it!")
if input=='3':
    import thread, time

    def input_thread(L):
        raw_input()
        L.append(None)
    
    def do_print():
        L = []
        thread.start_new_thread(input_thread, (L,))
        while 1:
            #time.sleep(.1)
            print "testing"
            if L: break
            #print "Hi Mom!"
            
    for x in range(2):
        raw_input("ready for next input?")
        do_print()

else:
    print("1, 2, or 3 please")
