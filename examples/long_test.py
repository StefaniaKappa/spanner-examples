#!/usr/bin/python
# -*- coding: utf-8 -*-

# import time
# import string
# import random

# for i in range(1, 10):
#   print('----' + ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(i*1000)) + '----', flush=True)
#   time.sleep(100)

# print("success")
# print("successfully")
# print("Failure")
# print("This is success!")
# print("This is successfully")
# print("success done")

import Spanner
from time import sleep 

def validate_dummy_test_case():
    Spanner.assertTrue(1);

if __name__ == "__main__":
    
    validate_dummy_test_case()
    print("Failure")
