# -*- coding: utf-8 -*-
"""
collect_public_ticker_ALL.py: loop for collect data
@ author: 5eo1ab
@ version: pilot test(v1)
"""

import os
import time
from XCoinAPI import XCoinPublic

WORK_DIR = '/'.join(os.getcwd().split('\\'))
OUT_DIR = '{}/public_ticker_ALL'.format(WORK_DIR)
print("Working Dir: {}\nOutput Dir: {}".format(WORK_DIR, OUT_DIR))

def set_directory(OUT_DIR):
	if os.path.exists(OUT_DIR) == False:
		os.makedirs(OUT_DIR)
	return None

if __name__ == '__main__':
	set_directory(OUT_DIR)
	while True:
		for i in range(120):
			xcoin = XCoinPublic() # default value: mode='ticker', currency='ALL'
			xcoin.dump(OUT_DIR)
			time.sleep(0.5)
		print(xcoin.get_now_strftime())
