# -*- coding: UTF-8 -*-
import hashlib, time, requests, json, sys, os
reload(sys)
sys.setdefaultencoding( "utf-8" ) 

class Resource(object):
	"""docstring for Resource"""
	__appId = ''
	__baseurl = ''
	__appCode = ''
	__headers= {}
	__sessionToken = ''

	def __init__(self, appId, appKey, baseurl=''):
		self.__appId = appId
		self.__baseurl = baseurl or "https://d.apicloud.com/mcm/api"
		timeStamp = int(time.time()*1000)
		self.__appCode = hashlib.sha1(appId + "UZ" + appKey + "UZ" + str(timeStamp)).hexdigest() + "." + str(timeStamp)
		self.__headers = {
			"X-APICloud-AppId":self.__appId,
			"X-APICloud-AppKey":self.__appCode
		}	
	def setSessionToken(self, token):
		self.__sessionToken = token

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
		if self.__sessionToken:
			self.__headers["authorization"] = self.__sessionToken

		attr = self.handleFile(attr)
		# print isinstance(attr, dict)
		headers = {
			"X-APICloud-AppId":self.__appId,
			"X-APICloud-AppKey":self.__appCode
		}	
		headers["Content-Type"] = "application/json"
		url = self.__baseurl + '/' + object

		r = requests.post(url, headers = headers, data = json.dumps(attr))
		return r.json()
		
	def getObject(self, object, id):
		if not object or not id:
			return {'status':0,'msg':'please pass the parameter!'}
		if self.__sessionToken:
			self.__headers["authorization"] = self.__sessionToken	
		url = self.__baseurl +'/' + object + '/' + id
		print self.__headers
		r = requests.get(url, headers = self.__headers)
		return r.json()

	def updateObject(self, object, id, attr):
		if not object or not id:
			return {'status':0,'msg':'please pass the parameter!'}
		if not attr:
			return {'status':0,'msg':'please update at lease one filed!'}
		attr = self.handleFile(attr)
		headers = {
			"X-APICloud-AppId":self.__appId,
			"X-APICloud-AppKey":self.__appCode
		}	
		headers["Content-Type"] = "application/json"
		url = self.__baseurl + '/' + object + '/' + id
		if self.__sessionToken:
			self.__headers["authorization"] = self.__sessionToken	
		r = requests.put(url, headers = headers, data = json.dumps(attr))
		return r.json()
	
	def getObjects(self, object):
		if not object:
			return {'status':0,'msg':'please pass the parameter!'}

		url = self.__baseurl +'/' + object
		if self.__sessionToken:
			self.__headers["authorization"] = self.__sessionToken	
		r = requests.get(url, headers = self.__headers)
		return r.json()

	def deleteObject(self, object, id):
		if not object or not id:
			return {'status':0,'msg':'please pass the parameter!'}
		url = self.__baseurl + '/' + object + '/' + id
		if self.__sessionToken:
			self.__headers["authorization"] = self.__sessionToken	
		r = requests.delete(url, headers = self.__headers)
		return r.json()

	def getObjectCount(self, object):
		if not object:
			return {'status':0,'msg':'please pass the parameter!'}
		url = self.__baseurl + '/' + object + '/count'
		if self.__sessionToken:
			self.__headers["authorization"] = self.__sessionToken
		r = requests.get(url, headers = self.__headers)
		return r.json()	

	def checkObjectExists(self, object, id):
		if not object or not id:
			return {'status':0,'msg':'please pass the parameter!'}
		url = self.__baseurl+ '/' + object + '/' + id + "/exists"
		if self.__sessionToken:
			self.__headers["authorization"] = self.__sessionToken
		r = requests.get(url, headers = self.__headers)
		return r.text	

###################################################
# relateion objects
###################################################

	def getRelationObject(self, object, id, relationObject):
		if not object or not id or not relationObject:
			return {'status':0,'msg':'please pass the parameter!'}
		url = self.__baseurl + '/' + object + '/' + id + '/' + relationObject
		# print url
		r = requests.get(url, headers = self.__headers)
		return r.json()	

	def createRelationObject(self, object, id, relationObject, attr):
		if not object or not id or not relationObject or not attr:
			return {'status':0,'msg':'please pass the parameter!'}
		attr = self.handleFile(attr)
		# print isinstance(attr, dict)
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
		if not object or not id or not relationObject:
			return {'status':0,'msg':'please pass the parameter!'}
		url = self.__baseurl + '/' + object + '/' + id + '/' + relationObject + '/count'
		r = requests.get(url, headers = self.__headers)
		return r.json()	

	def deleteRelationObject(self, object, id, relationObject):
		if not object or not id or not relationObject:
			return {'status':0,'msg':'please pass the parameter!'}
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
		if self.__sessionToken:
			self.__headers["authorization"] = self.__sessionToken
		r = requests.post(url, headers = headers, data = json.dumps(attr))
		return r.json()

	def userLogin(self, username, password):
		self.__headers["Content-Type"] = "application/x-www-form-urlencoded"
		if not username:
			return {'status':0,'msg':'user name can not be null'}
		if not password:
			return {'status':0,'msg':'pass cannot be null'}

		url = self.__baseurl+"/user/login"
		payload = {
			"username":username,
			"password": password
		}
		r = requests.post(url, headers = self.__headers, data = payload)
		return r.json()	

	def userLogout(self,token=''):
		token = token or self.__sessionToken
		if not token:
			return {'status':0,'msg':'please input a valid token!'}			
		self.__headers["authorization"] = token
		url = self.__baseurl+"/user/logout"
		r = requests.post(url, headers = self.__headers)
		return r.json()			

	def verifyEmail(self, attr):
		self.__headers["Content-Type"] = "application/json"
		if not attr:
			return {'status':0,'msg':'please pass parameter!'}
		
		if 'username' not in attr or not attr['username']:
			return {'status':0,'msg':'username cannot be null!'}
		
		if 'email' not in attr or not attr['email']:
			return {'status':0,'msg':'email is required'}
		
		if 'language' not in attr or not attr['language']:
			return {'status':0,'msg':'please input language!'}
		
		url = self.__baseurl + "/user/verifyEmail"
		if self.__sessionToken:
			self.__headers["authorization"] = self.__sessionToken
		r = requests.post(url, headers = self.__headers, data = json.dumps(attr))
		return r.json()			

	def resetRequest(self, attr):
		self.__headers["Content-Type"] = "application/json"
		if not attr:
			return {'status':0,'msg':'please pass parameter!'}
		
		if 'username' not in attr or not attr['username']:
			return {'status':0,'msg':'name cannot be null'}
		
		if 'email' not in attr or not attr['email']:
			return {'status':0,'msg':'email cannot be null'}
		
		url = self.__baseurl + "/user/resetRequest"
		if self.__sessionToken:
			self.__headers["authorization"] = self.__sessionToken
		r = requests.post(url, headers = self.__headers, data = json.dumps(attr))
		return r.json()	

	def getUserInfo(self,userId,authorization=''):
		self.__headers["Content-Type"] = "application/json"
		if len(authorization) > 0:
			self.__headers["authorization"] = authorization
		url = self.__baseurl + '/user/' + userId
		if self.__sessionToken:
			self.__headers["authorization"] = self.__sessionToken
		r = requests.get(url, headers = self.__headers)
		return r.json()	

	def updateUserInfo(self, attr):
		if not attr:
			return {'status':0,'msg':'please pass parameter!'}
		
		if 'userId' not in attr or not attr['userId']:
			return {'status':0,'msg':'userId cannot be null'}
		
		if 'authorization' in attr and len(attr['authorization']) > 0:
			self.__headers["authorization"] = attr['authorization']
			attr.pop('authorization')

		url = self.__baseurl + '/user/' + attr['userId']
		# print url
		attr.pop('userId')
		attr = self.handleFile(attr)
		headers["Content-Type"] = "application/json"
		if self.__sessionToken:
			self.__headers["authorization"] = self.__sessionToken
		r = requests.put(url, headers = self.__headers, data = json.dumps(attr))
		return r.json()

	def deleteUser(self,userId,authorization = ''):
		self.__headers["Content-Type"] = "application/json"
		if len(authorization) > 0:
			self.__headers["authorization"] = authorization
		url = self.__baseurl + '/user/' + userId
		if self.__sessionToken:
			self.__headers["authorization"] = self.__sessionToken
		r = requests.delete(url, headers = self.__headers)
		return r.json()	

###############################
# role related operation
###############################

	def createRole(self, attr):
		if not attr:
			return {'status':0,'msg':'please pass parameter!'}
		attr = self.handleFile(attr);
		headers = {
			"X-APICloud-AppId":self.__appId,
			"X-APICloud-AppKey":self.__appCode
		}	
		headers["Content-Type"] = "application/json"

		url = self.__baseurl + '/role'	
		if self.__sessionToken:
			self.__headers["authorization"] = self.__sessionToken
		r = requests.post(url, headers = headers, data = json.dumps(attr))
		return r.json()		

	def getRole(self, id):
		if not id:
			return {'status':0,'msg':'please pass parameter!'}
		url = self.__baseurl + '/role/' + id
		if self.__sessionToken:
			self.__headers["authorization"] = self.__sessionToken
		r = requests.get(url, headers = self.__headers)
		return r.json()

	def updateRole(self, id, attr):	
		if not id:
			return {'status':0,'msg':'please pass parameter!'}
		if not attr:
			return {'status':0,'msg':'please pass parameter!'};
		
		attr = self.handleFile(attr)
		self.__headers["Content-Type"] = "application/json; charset=UTF-8"	
		url = self.__baseurl + '/role/' + id
		if self.__sessionToken:
			self.__headers["authorization"] = self.__sessionToken
		r = requests.put(url, headers = self.__headers, data = json.dumps(attr))	
		return r.json()	

	def deleteRole(self, id):
		url = self.__baseurl + '/role/' + id
		if self.__sessionToken:
			self.__headers["authorization"] = self.__sessionToken
		r = requests.delete(url, headers = self.__headers)
		return r.json()	
	
####################################
# batch operation
####################################
	def batch(self, attr):
		if not attr:
			return {'status':0,'msg':'please pass parameter!'}
		self.__headers["Content-Type"] = "application/json"	
		url = self.__baseurl + '/batch'
		if self.__sessionToken:
			self.__headers["authorization"] = self.__sessionToken
		r = requests.post(url, headers = self.__headers, data = json.dumps(attr))
		return r.json()

####################################################################################
#查看参数中是否含有file对象，如果有的话，先上传，在将返回的信息替换掉原来的file对象
#param 
#attr : {col1: {isFile:True or False, path: 文件路径},col2:'some value'}
####################################################################################
	def handleFile(self, attr):
		# print attr
		for key in attr.keys():
			if 'isFile' in attr[key] and attr[key]['isFile']:
				if os.path.isfile(attr[key]['path']):
					# print attr[key]
					r = self.upload(attr[key]['path'])
					# print r
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
			return {'status':0, 'msg':'path cannot be null!'}
		if not os.path.isfile(filePath):
			return {'status':0, 'msg':'invalid file!'}
		url = self.__baseurl+"/file"
		self.__headers["ENCTYPE"] = "multipart/form-data" 
		fileName = os.path.basename(filePath)
		uploadFile = {'file': (fileName, open(filePath, 'rb'), fileType)}
		# print uploadFile
		if self.__sessionToken:
			self.__headers["authorization"] = self.__sessionToken
		r = requests.post(url, headers = self.__headers, files = uploadFile)
		# print 'upload return '+r.text
		return r.json()

####################################################################################
#updateModel
#param 
#object
#id
####################################################################################
	def updateModel(self, object, id, attr):
		if not object or not id or not attr:
			return {'status':0,'msg':'please pass parameter!'}
				
		self.__headers["Content-Type"] = "application/json"			
		url = self.__baseurl + '/' + object + '/'+ id
		if self.__sessionToken:
			self.__headers["authorization"] = self.__sessionToken
		r = requests.put(url, headers = self.__headers, data = json.dumps(attr))
		return r.json()

####################################################################################
#updateModel
#param 
#object
#id
####################################################################################
	def doFilterSearch(self, object, filter):
		if not object:
			return {'status':0,'msg':'please pass parameter!'}
		
		url = self.__baseurl + '/' +object+"?filter="
		url += json.dumps(filter, "utf-8")
		# url += json.dumps(filter)
		if self.__sessionToken:
			self.__headers["authorization"] = self.__sessionToken
		r = requests.get(url, headers = self.__headers)
		return r.json()