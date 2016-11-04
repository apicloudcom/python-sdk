# -*- coding: UTF-8 -*-
import simplejson
from Resource import Resource

datacloud = Resource('A6988846915732','391BB7B7-827D-1DE5-2F64-04339E801812','http://192.168.13.183/mcm/api')


#################user operation##############################
# print datacloud.createUser({"username":"abc","password":"123456","email":"xinghai.zhou@apicloud.com"})
r = datacloud.userLogin('zxh','123456')

datacloud.setSessionToken(r["id"])
# print datacloud.userLogout(r["id"])
# r = datacloud.verifyEmail({"username":"zxh","email":"xinghai.zhou@apicloud.com","language":"zh_CN"})
# print simplejson.dumps(r, ensure_ascii=False)
# print r['msg']
# print r['status']

# print datacloud.resetRequest({"username":"zxh","email":"xinghai.zhou@apicloud.com","language":"zh_CN"})
# print datacloud.getUserInfo('5576b9eec24a9b3c54f82203');
# print datacloud.updateUserInfo({'userId':'55796f23dfc407df41432f94','address':'dandong'})
# print datacloud.deleteUser('55796f23dfc407df41432f94');


#################object operation##############################
# print datacloud.createObject("company",{"address":"丹东1", "name":"aaa","icon":{"isFile":True,"path":"E:\\2007119124513598_2.jpg"},"icon2":{"isFile":True,"path":"E:\\2007119124513598_2.jpg"}})
# print datacloud.createObject("company",{"address":"germany", "name":"ccc","icon":{"url":"http://a82510f6efdff35a65fb.b0.upaiyun.com/apicloud/e96e53bb577560b2d5acb1e3ef7a492b.jpg","id":"5578114b85ff91bf364f0d6a","name":"2007119124513598_2.jpg"}})
# print datacloud.getObject('company','55828f4c291f49171a8dba9b')

# print datacloud.updateObject('company','5578125185ff91bf364f0d6c',{'address':'dandong',"icon":{"isFile":True,"path":"E:\\zhanqi.PNG"}})

# print datacloud.getObjects('company')
# print datacloud.deleteObject('company','557966eddfc407df41432f8f')
# print datacloud.getObjectCount('company')
# print datacloud.checkObjectExists('company','5578171085ff91bf364f0d6e')

#################relation operation##############################
# print datacloud.createRelationObject('company','557812cb85ff91bf364f0d6d','field',{'name':'arts'})
# print datacloud.getRelationObject('company','557812cb85ff91bf364f0d6d','field')
# print datacloud.getRelationObjectCount('company','557812cb85ff91bf364f0d6d','field')
# print datacloud.deleteRelationObject('company','557812cb85ff91bf364f0d6d','field')


#################role operation##############################
print datacloud.createRole({'name':'manager','description':'desc'});
print datacloud.getRole('5579748cdfc407df41432f95');
# print datacloud.updateRole('5579748cdfc407df41432f95',{'name':'manager11','description':'desc22'});
# print datacloud.deleteRole('5579748cdfc407df41432f95');


#################file operation##############################
# abc = datacloud.handleFile({'col1':{'isFile':True,'path':'E:\\2007119124513598_2.jpg'}, 'col2':'efg'})
# print isinstance(abc,dict)
# print datacloud.upload('E:\\2007119124513598_2.jpg','image/jpeg')
# files = {'files': open('E:\\apicloud-code\\python_cloud\\upload_file', 'rb')}


#################batch operation##############################
# print datacloud.batch({"requests":[{
# 		"method":"GET",
# 		"path":"/mcm/api/file"
# 	},
# 	{
# 		"method":"GET",
# 		"path":"/mcm/api/file/count"
# 	}]})
#################model operation##############################
# print datacloud.updateModel('company','557812cb85ff91bf364f0d6d',{"$inc": { "count": 2}, "address":"APICloud"})


#################filter operation##############################
# print datacloud.doFilterSearch('company', { "where": {"id": "557812cb85ff91bf364f0d6d"}})
# print datacloud.doFilterSearch('company', {"where":{"address":{"inq":["germany","china"]}}})
# print datacloud.doFilterSearch('company', {"include":"field"},"where")
# print datacloud.doFilterSearch('company', { "fields": {"address": "true","quantity":"true"},"where":{"and":[{"id": "557812cb85ff91bf364f0d6d"},{"id": "5578114b85ff91bf364f0d6b"}]},"limit":5})
# print datacloud.doFilterSearch('company', { "limit": 2})
