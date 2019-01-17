#!/usr/bin/python
# -*- coding: utf-8 -*-

import time

for i in range(100):
  print('----' + ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(i)) + '----', flush=True)
  time.sleep(1)
