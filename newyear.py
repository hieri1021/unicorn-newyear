#from tkinter import *
import time
import datetime
import pygame

newyear = datetime.datetime(year=2024, month=1, day=1)
#print(abs(newyear - datetime.datetime.now()).seconds)
#print(type(abs(newyear - datetime.datetime.now()).total_seconds()))

pygame.mixer.init(frequency = 44100)
pygame.mixer.music.load("unicorn.mp3")

def main():
    while True:
        try:
            ptime = datetime.datetime.now()
        
        except KeyboardInterrupt:
            break
        
        else:
            #print(f'\r{ptime}',end='')
            print(f'\r{newyear - ptime}', end='')
            
            if abs(newyear - ptime).seconds == 41:
                pygame.mixer.music.play(1)
            
            time.sleep(0.05)

if __name__ == "__main__":
    main()