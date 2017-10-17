"""
collect_public_ticker_ALL.py: loop for collect data
@ author: 5eo1ab
@ version: public stage(v1)
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

	p_seq = 0
	while True:
		xcoin = XCoinPublic()
		xcoin.dump(OUT_DIR)
		time.sleep(1)
		p_seq += 1
		if p_seq == 100:
			print(xcoin.get_now())
			p_seq = 0
