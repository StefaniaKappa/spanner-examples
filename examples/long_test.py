#!/usr/bin/python
# -*- coding: utf-8 -*-

import time

for i in range(1, 10):
  print('----' + ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(i*1000)) + '----', flush=True)
  time.sleep(1)

print("success")
print("successfully")
print("Failure")
print("This is success!")
print("This is successfully")
print("success done")
