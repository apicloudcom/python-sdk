# -*- coding: UTF-8 -*-
from dataCloud import DataCloud

datacloud = DataCloud('A6988846915732','391BB7B7-827D-1DE5-2F64-04339E801812','http://192.168.13.183/mcm/api')
# print datacloud.createObject("company",{"address":"france", "name":"aaa","icon":{"isFile":True,"path":"E:\\2007119124513598_2.jpg"}})
# print datacloud.createObject("company",{"address":"germany", "name":"ccc","icon":{"url":"http://a82510f6efdff35a65fb.b0.upaiyun.com/apicloud/e96e53bb577560b2d5acb1e3ef7a492b.jpg","id":"5578114b85ff91bf364f0d6a","name":"2007119124513598_2.jpg"}})
# print datacloud.getObject('company','557966eddfc407df41432f8f')
# print datacloud.updateObject('company','557966eddfc407df41432f8f',{'address':'dandong'})
r = datacloud.updateObject('company','557966eddfc407df41432f8f',{})
print r['status']
print r['msg']
# print datacloud.deleteObject('company','557966eddfc407df41432f8f')
# print datacloud.getObjectCount('company')
# print datacloud.checkObjectExists('company','5579691adfc407df41432f91')


# print datacloud.getRelationObject('company','5579691adfc407df41432f91','field')
# print datacloud.createRelationObject('company','5579691adfc407df41432f91','field',{'name':'arts'})
# print datacloud.getRelationObjectCount('company','5579691adfc407df41432f91','field')
# print datacloud.deleteRelationObject('company','5579691adfc407df41432f91','field')

# print datacloud.createUser({"username":"zxh","password":"123456","email":"xinghai.zhou@apicloud.com"})
# print datacloud.userLogin('zxh','123456')
# print datacloud.userLogout('eOU5DONp99HgGjMOz50EOOMijthDTbtiAyZ95gL6Qmw7SIcADBNbPnv1GRBUDaoQ')
# r = datacloud.verifyEmail({"username":"zxh","email":"xinghai.zhou@apicloud.com","language":"zh_CN"})
# print r
# print r['msg']
# print r['status']
# print r['msg'].decode("utf-8")

# print datacloud.resetRequest({"username":"zxh","email":"xinghai.zhou@apicloud.com","language":"zh_CN"})
# print datacloud.getUserInfo('55796f23dfc407df41432f94');
# print datacloud.updateUserInfo({'userId':'55796f23dfc407df41432f94','address':'dandong'})
# print datacloud.deleteUser('55796f23dfc407df41432f94');

# print datacloud.createRole({'name':'manager','description':'desc'});
# print datacloud.getRole('5579748cdfc407df41432f95');
# print datacloud.updateRole('5579748cdfc407df41432f95',{'name':'manager11','description':'desc22'});
# print datacloud.deleteRole('5579748cdfc407df41432f95');

# abc = datacloud.handleFile({'col1':{'isFile':True,'path':'E:\\2007119124513598_2.jpg'}, 'col2':'efg'})
# print isinstance(abc,dict)
# print datacloud.upload('E:\\2007119124513598_2.jpg','image/jpeg')
# files = {'files': open('E:\\apicloud-code\\python_cloud\\upload_file', 'rb')}