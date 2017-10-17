import json
from urllib import request

class XCoinPublic:
	
	def __init__(self, mode='ticker', currency='ALL'):
		# {mode} = ticker (bithumb 거래소 마지막 거래 정보)
		# 		 = orderbook (bithumb 거래소 판/구매 등록 대기 또는 거래 중 내역 정보)
		#		 = recent_transactions (bithumb 거래소 거래 체결 완료 내역)
		# {currency} = BTC, ETH, DASH, LTC, ETC, XRP, BCH, XMR, ZEC (기본값: BTC), ALL(전체)
		self.base_url = "https://api.bithumb.com/public/{}/{}".format(mode, currency)
		self.res_data = self.__call__()
		self.d_code = "{}_{}".format(mode, currency)
		return None

	def __call__(self):
		res = request.urlopen(self.base_url).read()
		#print(type(res)) 	# <class 'bytes'>
		json_res = json.loads(res.decode('utf-8'))
		if json_res['status'] != '0000':
			print(json_res['status'])
			return None
		return json_res['data']

	def get_data(self):
		return self.res_data

	def dump(self, fpath=None):
		import datetime
		if fpath is None:
			import os
			fpath = '/'.join(os.getcwd().split('\\'))
		now = datetime.datetime.now().strftime('%y%m%d-%H%M%S')
		with open(fpath+'/xcoin-public_{}_{}.json'.format(self.d_code, now), 'w') as f:
			json.dump(self.res_data, f)
		return None


if __name__ == '__main__':
	xcoin = XCoinPublic()
	print(xcoin.get_data())
	xcoin.dump()
