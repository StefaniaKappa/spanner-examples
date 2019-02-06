#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import string
import random

for i in range(1, 10):
  print('----' + ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(i*1000)) + '----', flush=True)
  time.sleep(100)

print("success")
print("successfully")
print("Failure")
print("This is success!")
print("This is successfully")
print("success done")
