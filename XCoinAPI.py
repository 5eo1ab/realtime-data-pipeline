# -*- coding: utf-8 -*-
"""
XCoinAPI.py: Customizing Bithumb API
@ author: 5eo1ab
@ version: public stage(v1)
"""

import json
from urllib import request
import datetime

class XCoinPublic:
	def __init__(self, mode='ticker', currency='ALL'):
		# {mode} = ticker (bithumb 거래소 마지막 거래 정보)
		#		 , orderbook (bithumb 거래소 판매, 구매 등록 대기 또는 거래 중 내역 정보)
		#		 , recent_transactions (bithumb 거래소 거래 체결 완료 내역)
		# {currency} = BTC, ETH, DASH, LTC, ETC, XRP, BCH, XMR, ZEC (기본값: BTC), ALL(전체)
		self.base_url = "https://api.bithumb.com/public/{}/{}".format(mode, currency)
		self.res_data = self.__call__()
		self.d_code = "{}_{}".format(mode, currency)
		#self.now = datetime.datetime.now().strftime('%y%m%d-%H%M%S')
		self.now = int(datetime.datetime.today().timestamp()*1000)
		return None

	def __call__(self):
		res = request.urlopen(self.base_url).read()
		#print(type(res)) 	# <class 'bytes'>
		json_res = json.loads(res.decode('utf-8'))
		if json_res['status'] != '0000':
			print(json_res['status'])
			return None
		return json_res['data']

	def dump(self, fpath=None):
		if fpath is None:
			import os
			fpath = '/'.join(os.getcwd().split('\\'))
		with open(fpath+'/{}_{}.json'.format(self.d_code, self.now), 'w') as f:
			json.dump(self.res_data, f)
		return None

	def __ts2strftime__(ts):
		res = datetime.datetime.fromtimestamp(ts/1000).strftime("%Y-%m-%d %H:%M:%S")
		return res

	def get_data(self):		return self.res_data
	def get_now(self):		return self.now
	def get_now_strftime(self):	return self.__ts2strftime__(self.now)

if __name__ == '__main__':
	xcoin = XCoinPublic()
	print(xcoin.get_data())
	print("timestamp: {}".format(xcoin.now))
	print(xcoin.get_now_strftime())
	#xcoin.dump()
