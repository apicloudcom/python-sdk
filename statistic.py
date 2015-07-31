#-*-coding:utf-8-*- 

import hashlib, time, requests, json

class Statistics(object):
	"""docstring for Statistics"""
	__appId = ''
	__baseurl = ''
	__appCode = ''
	
	def __init__(self, appId, appKey, baseurl=''):
		self.__appId = appId
		self.__baseurl = baseurl or "https://r.apicloud.com/analytics/";
		self.__appCode = hashlib.sha1(appId + "UZ" + appKey + "UZ" + str(int(time.time()))).hexdigest() + "." + str(int(time.time()));

 #该接口主要用于获取用户指定应用ID及时间范围内的相关应用统计数据信息。
 #params
 # startDate – 开始时间 格式：YYYY-MM-DD 例如：2014-10-10
 # endDate – 结束时间 格式：YYYY-MM-DD
 	def getAppStatisticDataById(self, startDate, endDate):
		headers = {
			"X-APICloud-AppId":self.__appId,
			"X-APICloud-AppKey":self.__appCode
		}
		payload = {
			"startDate":startDate,
			"endDate":endDate
		}
		r = requests.post(self.__baseurl+'/getAppStatisticDataById', data = payload, headers = headers)
		return r.json()

# 该接口主要用于获取用户指定应用ID及时间范围内相关应用各版本的统计数据信息。
# params
# startDate – 开始时间 格式：YYYY-MM-DD 例如：2014-10-10
# endDate – 结束时间 格式：YYYY-MM-DD
 	def getVersionsStatisticDataById(self, startDate, endDate):
		headers = {
			"X-APICloud-AppId":self.__appId,
			"X-APICloud-AppKey":self.__appCode
		}
		payload = {
			"startDate":startDate,
			"endDate":endDate
		}
		r = requests.post(self.__baseurl+'/getVersionsStatisticDataById', data = payload, headers = headers)
		return r.json()

# 该接口主要用于获取用户指定应用ID及时间范围内的应用下各版本地理分布统计数据信息。
# params
# startDate – 开始时间 格式：YYYY-MM-DD 例如：2014-10-10
# endDate – 结束时间 格式：YYYY-MM-DD
# versionCode  - 版本
  	def getGeoStatisticDataById(self, startDate, endDate, versionCode):
		headers = {
			"X-APICloud-AppId":self.__appId,
			"X-APICloud-AppKey":self.__appCode
		}
		payload = {
			"startDate":startDate,
			"endDate":endDate,
			"versionCode":versionCode
		}
		r = requests.post(self.__baseurl+'/getGeoStatisticDataById', data = payload, headers = headers)
		return r.json()

# 该接口主要用于获取用户指定应用ID及时间范围内的应用下各版本设备信息分布统计数据信息。
# params
# startDate – 开始时间 格式：YYYY-MM-DD 例如：2014-10-10
# endDate – 结束时间 格式：YYYY-MM-DD
  	def getDeviceStatisticDataById(self, startDate, endDate):
		headers = {
			"X-APICloud-AppId":self.__appId,
			"X-APICloud-AppKey":self.__appCode
		}
		payload = {
			"startDate":startDate,
			"endDate":endDate
		}
		r = requests.post(self.__baseurl+'/getDeviceStatisticDataById', data = payload, headers = headers)
		return r.json()

# 该接口主要用于获取用户指定应用ID及时间范围内的应用下各版本异常错误统计数据信息。
# params
# startDate – 开始时间 格式：YYYY-MM-DD 例如：2014-10-10
# endDate – 结束时间 格式：YYYY-MM-DD
 	def getExceptionsStatisticDataById(self, startDate, endDate):
		headers = {
			"X-APICloud-AppId":self.__appId,
			"X-APICloud-AppKey":self.__appCode
		}
		payload = {
			"startDate":startDate,
			"endDate":endDate
		}
		r = requests.post(self.__baseurl+'/getExceptionsStatisticDataById', data = payload, headers = headers)
		return r.json()

# 该接口主要用于根据应用异常错误摘要获取异常错误详细信息
# params
# title – 错误摘要信息
 	def getExceptionsDetailByTitle(self, title):
		headers = {
			"X-APICloud-AppId":self.__appId,
			"X-APICloud-AppKey":self.__appCode
		}
		payload = {
			"title":title
		}
		r = requests.post(self.__baseurl+'/getExceptionsDetailByTitle', data = payload, headers = headers)
		return r.json()

# 该接口主要用于获得当前设置对象的内部配置信息
	def printConfigVal(self):
		return {
			'appId': self.__appId,
			'appCode': self.__appCode,
			'url': self.__baseurl
			}


class Push(object):
	__appId = ''
	__baseurl = ''
	__appCode = ''	
	"""docstring for Push"""
	def __init__(self, appId, appKey, baseurl=''):
		self.__appId = appId
		self.__baseurl = baseurl or "https://p.apicloud.com/api/push/message";
		self.__appCode = hashlib.sha1(appId + "UZ" + appKey + "UZ" + str(int(time.time()))).hexdigest() + "." + str(int(time.time()));
# body
#	 title–消息标题，
#	 content – 消息内容
#	 type – 消息类型，1:消息 2:通知
#	 timer – 定时消息发送时间。定时不为空则为定时消息，毫秒数。可选参数。
#	 platform - 0:全部平台，1：ios, 2：android
#	 groupName - 推送组名，多个组用英文逗号隔开.默认:全部组。eg.group1,group2 .
#	 userIds - 推送用户id, 多个用户用英文逗号分隔，eg. user1,user2。

	def message(self, payload):
		headers = {
			"X-APICloud-AppId":self.__appId,
			"X-APICloud-AppKey":self.__appCode
		}
		if not isinstance(payload, dict):
			return {
				'status':0, 
				'msg':'please provided correct parameters!'
			}
		if 'title' not in payload or 'content' not in payload or 'type' not in payload or 'platform' not in payload:
			return {
				'status':0, 
				'msg':'please provided correct parameters!'
			}
		r = requests.post(self.__baseurl, data = payload, headers = headers)
		return r.json()
	
	# 该接口主要用于获得当前设置对象的内部配置信息
	def printConfigVal(self):
		return {
			'appId': self.__appId,
			'appCode': self.__appCode,
			'url': self.__baseurl
			}