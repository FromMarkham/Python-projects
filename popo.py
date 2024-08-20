import simpleaudio as sa
#import time
#import datetime


sound='Clicky.wav'

sound2 = sa.WaveObject.from_wave_file(sound)

for i in range(100):
    #time.sleep(1)
    sound2.play()
    
#https://www.tutorialspoint.com/How-to-install-a-Python-package-into-a-different-directory-using-pip
#https://www.google.com/search?q=directory+compuying&rlz=1C5MACD_enCA1034CA1034&oq=directory+compuying&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIJCAEQABgNGIAEMgkIAhAAGA0YgAQyCggDEAAYBRgNGB4yCggEEAAYBRgNGB4yCggFEAAYBRgNGB4yCggGEAAYBRgNGB4yCggHEAAYBRgNGB4yCggIEAAYBRgNGB4yCggJEAAYBRgNGB7SAQgzNTEzajBqNKgCALACAQ&sourceid=chrome&ie=UTF-8
