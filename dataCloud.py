# -*- coding: UTF-8 -*-
import hashlib, time, requests, json, sys, os
reload(sys)
sys.setdefaultencoding( "utf-8" ) 

class DataCloud(object):
	"""docstring for DataCloud"""
	__appId = ''
	__baseurl = ''
	__appCode = ''
	__headers= {}

	def __init__(self, appId, appKey, baseurl=''):
		self.__appId = appId
		self.__baseurl = baseurl or "https://d.apicloud.com/mcm/api";
		timeStamp = int(time.time())
		self.__appCode = hashlib.sha1(appId + "UZ" + appKey + "UZ" + str(timeStamp)).hexdigest() + "." + str(timeStamp);
		self.__headers = {
			"X-APICloud-AppId":self.__appId,
			"X-APICloud-AppKey":self.__appCode
		}		

###########################################
# 对象相关API
# "icon": {
#    "url": "http://a82510f6efdff35a65fb.b0.upaiyun.com/apicloud/e946ec7a894236e18ad52e4e251dc156.jpg",
#    "name": "2007119124513598_2.jpg",
#    "id": "5578015085ff91bf364f0d58"
#  },
############################################		
	def createObject(self, object, attr):
		if not attr:
			attr = {}
		# print attr
		
		attr = self.handleFile(attr)
		# print isinstance(attr, dict)
		headers = {
			"X-APICloud-AppId":self.__appId,
			"X-APICloud-AppKey":self.__appCode
		}	
		headers["Content-Type"] = "application/json"
		url = self.__baseurl + '/' + object
		print 'usl is '+url
		r = requests.post(url, headers = headers, data = json.dumps(attr))
		# print r.request.headers
		# print r.request.body
		return r.json()
		
	def getObject(self, object, id):
		self.__headers["Content-Type"] = "application/json"
		url = self.__baseurl +'/' + object + '/' + id
		r = requests.get(url, headers = self.__headers)
		return r.json()

	def updateObject(self, object, id, attr):
		self.__headers["Content-Type"] = "application/json"
		if not attr:
			# return {'status':0,'msg':'请至少更新一个字段'}
			return {'status':0,'msg':'please update at lease one filed!'}
		attr = self.handleFile(attr)
		headers = {
			"X-APICloud-AppId":self.__appId,
			"X-APICloud-AppKey":self.__appCode
		}	
		headers["Content-Type"] = "application/json"
		url = self.__baseurl + '/' + object + '/' + id
		r = requests.put(url, headers = headers, data = json.dumps(attr))
		return r.json()
		

	def deleteObject(self, object, id):
		url = self.__baseurl + '/' + object + '/' + id
		r = requests.delete(url, headers = self.__headers)
		return r.json()

	def getObjectCount(self, object):
		url = self.__baseurl + '/' + object + '/count'
		r = requests.get(url, headers = self.__headers)
		return r.json()	

	def checkObjectExists(self, object, id):
		url = self.__baseurl+ '/' + object + '/' + id + "/exists"
		r = requests.get(url, headers = self.__headers)
		return r.text	

###################################################
# relateion objects
###################################################

	def getRelationObject(self, object, id, relationObject):
		url = self.__baseurl + '/' + object + '/' + id + '/' + relationObject
		print url
		r = requests.get(url, headers = self.__headers)
		return r.json()	

	def createRelationObject(self, object, id, relationObject, attr):
		attr = self.handleFile(attr)
		print isinstance(attr, dict)
		print attr
		headers = {
			"X-APICloud-AppId":self.__appId,
			"X-APICloud-AppKey":self.__appCode
		}	
		headers["Content-Type"] = "application/json"
		url = self.__baseurl + '/' + object+"/"+id+"/"+relationObject;
		# sean 
		r = requests.post(url, headers = headers, data = json.dumps(attr))
		return r.text

	def getRelationObjectCount(self, object, id, relationObject):
		url = self.__baseurl + '/' + object + '/' + id + '/' + relationObject + '/count'
		r = requests.get(url, headers = self.__headers)
		return r.json()	

	def deleteRelationObject(self, object, id, relationObject):
		url = self.__baseurl + '/' + object + '/' + id + '/' + relationObject
		# print url
		r = requests.delete(url, headers = self.__headers)
		return r.json()	

##############################
#user related operation
##############################		

	def createUser(self, attr):
		if not attr:
			# return {'status':0,'msg':'请传递参数'}
			return {'status':0,'msg':'please input parameters'}
		
		if 'username' not in attr or not attr['username']:
			# return {'status':0,'msg':'姓名不能为空'}
			return {'status':0,'msg':'user name can not be null'}
		
		if 'password' not in attr or not attr['password']:
			# return {'status':0,'msg':'密码不能为空'}
			return {'status':0,'msg':'pass cannot be null'}
		
		attr = self.handleFile(attr)
		headers = {
			"X-APICloud-AppId":self.__appId,
			"X-APICloud-AppKey":self.__appCode
		}	
		headers["Content-Type"] = "application/json"
		
		url = self.__baseurl+"/user"
		r = requests.post(url, headers = headers, data = json.dumps(attr))
		return r.json()

	def userLogin(self, username, password):
		# self.__headers["Content-Type"] = "application/json"
		self.__headers["Content-Type"] = "application/x-www-form-urlencoded"
		if not username:
			# return {'status':0,'msg':'姓名不能为空'}
			return {'status':0,'msg':'user name can not be null'}
		
		if not password:
			# return {'status':0,'msg':'密码不能为空'}
			return {'status':0,'msg':'pass cannot be null'}

		url = self.__baseurl+"/user/login"
		payload = {
			"username":username,
			"password": password
		}
		r = requests.post(url, headers = self.__headers, data = payload)
		return r.json()	

	def userLogout(self, loginId):
		self.__headers["authorization"] = loginId;
		if not loginId:
			# return {'status':0,'msg':'用户登录ID不能为空'}
			return {'status':0,'msg':'user id can not be null'}
		url = self.__baseurl+"/user/logout"
		r = requests.post(url, headers = self.__headers)
		return r.json()			

	def verifyEmail(self, attr):
		self.__headers["Content-Type"] = "application/json"
		if not attr:
			# return {'status':0,'msg':'请传递参数'}
			return {'status':0,'msg':'pls pass parameter'}
		
		if 'username' not in attr or not attr['username']:
			return {'status':0,'msg':'姓名不能为空'}
		
		if 'email' not in attr or not attr['email']:
			return {'status':0,'msg':'email is required'}
		
		if 'language' not in attr or not attr['language']:
			return {'status':0,'msg':'pls add language'}			
		
		url = self.__baseurl + "/user/verifyEmail";
		
		r = requests.post(url, headers = self.__headers, data = json.dumps(attr))
		return r.json()			

	def resetRequest(self, attr):
		self.__headers["Content-Type"] = "application/json"
		
		if not attr:
			return {'status':0,'msg':'请传递参数'}
		
		if 'username' not in attr or not attr['username']:
			return {'status':0,'msg':'姓名不能为空'}
		
		if 'email' not in attr or not attr['email']:
			return {'status':0,'msg':'邮箱不能为空'}
		
		url = self.__baseurl + "/user/resetRequest";
		r = requests.post(url, headers = self.__headers, data = json.dumps(attr))
		return r.json()	

	def getUserInfo(self,userId,authorization=''):
		self.__headers["Content-Type"] = "application/json"
		if len(authorization) > 0:
			self.__headers["authorization"] = authorization
		url = self.__baseurl + '/user/' + userId
		r = requests.get(url, headers = self.__headers)
		return r.json()	

	def updateUserInfo(self, attr):
		self.__headers["Content-Type"] = "application/json"
		
		if not attr:
			return {'status':0,'msg':'请传递参数'}
		
		if 'userId' not in attr or not attr['userId']:
			return {'status':0,'msg':'userId不能为空'}
		
		if 'authorization' in attr and len(attr['authorization']) > 0:
			self.__headers["authorization"] = attr['authorization']
			attr.pop('authorization')

		url = self.__baseurl + '/user/' + attr['userId']
		print url
		attr.pop('userId')
		r = requests.put(url, headers = self.__headers, data = json.dumps(attr))
		return r.json()

	def deleteUser(self,userId,authorization = ''):
		self.__headers["Content-Type"] = "application/json"
		if len(authorization) > 0:
			self.__headers["authorization"] = authorization
		url = self.__baseurl + '/user/' + userId
		r = requests.delete(url, headers = self.__headers)
		return r.json()	

###############################
# role related operation
###############################

	def createRole(self, attr):
		if not attr:
			return {'status':0,'msg':'请传递参数'}
		attr = self.handleFile(attr);
		headers = {
			"X-APICloud-AppId":self.__appId,
			"X-APICloud-AppKey":self.__appCode
		}	
		headers["Content-Type"] = "application/json"

		url = self.__baseurl + '/role'	
		r = requests.post(url, headers = headers, data = json.dumps(attr))
		return r.json()		

	def getRole(self, id):
		url = self.__baseurl + '/role/' + id
		r = requests.get(url, headers = self.__headers)
		return r.json()

	def updateRole(self, id, attr):	
		self.__headers["Content-Type"] = "application/x-www-form-urlencoded; charset=UTF-8"
		if not attr:
			return {'status':0,'msg':'请传递参数'};
		
		url = self.__baseurl + '/role/' + id;
		r = requests.put(url, headers = self.__headers, data = attr)	
		return r.json()	

	def deleteRole(self, id):
		url = self.__baseurl + '/role/' + id;
		r = requests.delete(url, headers = self.__headers)
		return r.json()	
	
####################################
# batch operation
####################################
	def batch(self, attr):
		if not attr:
			return {'status':0,'msg':'请传递参数'}
		url = self.__baseurl + '/batch'
		r = requests.post(url, headers = self.__headers, data = attr)
		return r.json()


	def updateModel(self, object, id, params):
		if params is Null:
			return {'status':0,'msg':'请传递参数'}
				
		url = self.__baseurl +object+"/"+id
		r = requests.put(url, headers = self.__headers)
		return r.json()

	def doFilterSearch(self, object, filter):
		if object is Null:
			return {'status':0,'msg':'请确定查询对象'}
		
		url = self.__baseurl +object+"?filter=";
		# url += URLEncoder.encode(filter, "utf-8");
		r = requests.get(url, headers = self.__headers)
		return r.json()

####################################################################################
#查看参数中是否含有file对象，如果有的话，先上传，在将返回的信息替换掉原来的file对象
#param 
#attr : {col1: {isFile:True or False, path: 文件路径},col2:'some value'}
####################################################################################
	def handleFile(self, attr):
		print attr
		for key in attr.keys():
			if 'isFile' in attr[key] and attr[key]['isFile']:
				if os.path.isfile(attr[key]['path']):
					print attr[key]
					r = self.upload(attr[key]['path'])
					print r

					if 'url' in r:
						attr[key]={}
						attr[key]['id'] = r['id']
						attr[key]['url'] = r['url']
						attr[key]['name'] = r['name']

					else:
						attr.pop([key])	
				else:
					attr.pop([key])
		return attr
			
####################################################################################
#根据filePath上传文件内容
#param 
#filePath 文件路径
#fileType 上传的文件类型，默认为（'application/octet-stream'）
####################################################################################	

	def upload(self, filePath,fileType = 'application/octet-stream'):
		if not filePath:
			return {'status':0, 'msg':'路径不能为空'}
		if not os.path.isfile(filePath):
			return {'status':0, 'msg':'invalid file'}
		url = self.__baseurl+"/file"
		self.__headers["ENCTYPE"] = "multipart/form-data" 
		fileName = os.path.basename(filePath)
		filea = {'file': (fileName, open(filePath, 'rb'), fileType)}
		print filea
		r = requests.post(url, headers = self.__headers, files = filea)
		print 'upload return '+r.text
		return r.json()

