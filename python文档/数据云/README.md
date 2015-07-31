
##概述

APICloud的 Python SDK 基于python 第三方模块requests创建的工具类,将数据云Api以面向对象的思想加以封装,支持对象化操作,只需要在你的代码中引入Resource类,便可以轻松完成数据云相关api接口的调用,操作数据云上的数据获取符合条件的数据.使用时请使用pip安装requests模块。<br>
SDK只对数据云的API进行封装，返回值不做任何修改，具体返回内容请参照数据云API的相关文档。


###**构造器**


```Python构造器：
Resource(appId, appKey, url);
```

####参数

appId：

- 类型：字符串
- 默认值：无
- 描述：应用的id，在APICloud上应用概览里获取，不能为空

appKey：

- 类型：字符串
- 默认值：无
- 描述：应用的安全校验Key，在APICloud上应用概览里获取，不能为空

url：

- 类型：字符串
- 默认值：https://d.apicloud.com/mcm/api
- 描述：应用服务器地址，可为空，为空时默认为数据服务器的https链接

####示例代码

```
client = Resource(appId, appKey);
```

####响应格式

对于所有的请求的响应格式都是一个 JSON 对象。 一个请求是否成功是由 HTTP 状态码标明的。一个 2XX 的状态码表示成功，而一个 4XX 表示请求失败。当一个请求失败时响应的主体仍然是一个 JSON 对象，但是总是会包含 code。 您可以用它们来进行调试。

####设置session信息
对于设置了权限的表的操作，需要提供用户登录后的session信息。我们提供下边的接口设置<br>
setSessionToken(token),其中token 为登录后的sessionId。之后所有操作直接调用相关接口即可完成。

##RESTful对象基本操作
###**1.创建对象**

向对象插入一条数据,支持对文件对象的上传操作，即如果对应的列存储的是文件对象，则该接口会自动把文件对象上传并记录上传地址到表的指定域中。如果上传的是文件对象则确保格式为{“isFile”:True, “path”: “文件路径”}。<br>
createObject(object, attr)

####参数
object

- 类型：字符串
- 默认值：无
- 描述：对象名称

attr

- 类型：JSON对象
- 默认值：无
- 描述：待插入的键值对，支持对文件对象的上传操作。

####示例代码

datacloud.createObject("company",{"address":"Beijing", "name":"apicloud"})


###**2.获取对象某一主键id的条目内容**

获取对象某一主键id的数据<br>
getObject(object, id)

####参数
object

- 类型：字符串
- 默认值：无
- 描述：对象名称

id

- 类型：字符串
- 默认值：无
- 描述：对象主键id

####示例代码

datacloud.getObject("company","557966eddfc407df41432f8f")



###**3.更新对象**

更新对象中以某一主键为id的条目的内容
updateObject(object, id, attr)

####参数
object

- 类型：字符串
- 默认值：无
- 描述：对象名称

id

- 类型：字符串
- 默认值：无
- 描述：获取的对象主键id

attr

- 类型：JSON对象
- 默认值：无
- 描述：待更新的键值对

####示例代码

datacloud.updateObject("company","557966eddfc407df41432f8f",{"address":"Beijing"})

###**4.获取对象全部内容**

获取对象中的全部内容<br>
getObjects(object)

####参数
object

- 类型：字符串
- 默认值：无
- 描述：对象名称

####示例代码

datacloud.getObjects("company")


###**5.删除对象**

删除对应对象中指定id的数据
deleteObject(object, id)

####参数
object

- 类型：字符串
- 默认值：无
- 描述：对象名称

id

- 类型：字符串
- 默认值：无
- 描述：待删除的键id

####示例代码

datacloud.deleteObject("company","557966eddfc407df41432f8f")


###**6.统计对象数量**

统计对象中数据条目数量<br>
getObjectCount(object)

####参数
object

- 类型：字符串
- 默认值：无
- 描述：对象名称

####示例代码

datacloud.getObjectCount("company")


###**7.判断对象是否存在**

判断对象中给定id的数据是否存在
checkObjectExists(object, id)

####参数
object

- 类型：字符串
- 默认值：无
- 描述：对象名称

id

- 类型：字符串
- 默认值：无
- 描述：对象的Id值

####示例代码

datacloud.checkObjectExists("company","557966eddfc407df41432f8f")

</br>


##**Relation对象相关接口**

###**1.获取关联对象数据**

获取指定对象中指定id关联对象的数据<br>
getRelationObject(object, id, relationObject)

####参数
object

- 类型：字符串
- 默认值：无
- 描述：对象名称

id

- 类型：字符串
- 默认值：无
- 描述：关联的数据Id

relationObject

- 类型：字符串
- 默认值：无
- 描述：关联对象名称

####示例代码

datacloud.getRelationObject('company','5579691adfc407df42f91','field')


###**2.在关联对象插入数据**

向关联对象中插入一条数据
createRelationObject(object, id, relationObject, attr)

####参数
object

- 类型：字符串
- 默认值：无
- 描述：对象名称

id

- 类型：字符串
- 默认值：无
- 描述：数据Id

relationObject

- 类型：字符串
- 默认值：无
- 描述：关联对象名称

attr

- 类型：JSON对象
- 默认值：无
- 描述：待插入的关联对象的数据

####示例代码

datacloud.createRelationObject('company','5579691adfc407df414f91','field',{'name':'arts'})


###**3.统计关联对象数量**

统计关联对象的数据条目数量<br>
getRelationObjectCount(object, id, relationObject)

####参数

object

- 类型：字符串
- 默认值：无
- 描述：对象名称

id

- 类型：字符串
- 默认值：无
- 描述：数据Id

relationObject

- 类型：字符串
- 默认值：无
- 描述：关联对象名称

####示例代码

datacloud.getRelationObjectCount('company','5579691adfc7df41432f91','field')


###**4.删除关联对象数据**

删除指定id所关联对象的所有数据<br>
deleteRelationObject(object, id, relationObject)

object

- 类型：字符串
- 默认值：无
- 描述：对象名称

id

- 类型：字符串
- 默认值：无
- 描述：数据Id

relationObject

- 类型：字符串
- 默认值：无
- 描述：关联对象名称

####示例代码

datacloud.deleteRelationObject('company','5579691ad07df41432f91','field')

<br>

##**用户**
###**1.新增用户**

新增用户<br>
createUser(attr):

####参数

attr

- 类型：JSON对象
- 默认值：无
- 描述：待插入的用户信息

####示例代码

datacloud.createUser({"username":"apicloud","password":"123456","email":"id@apicloud.com"})


###**2.登录**

用户登录<br>
userLogin(username, password)

####参数
username

- 类型：字符串
- 默认值：无
- 描述：用户名

password

- 类型：字符串
- 默认值：无
- 描述：密码

####示例代码

datacloud.userLogin('zxh','123456')


###**3.退出登录**

退出登录<br>
userLogout(loginId)

####参数
loginId

- 类型：字符串
- 默认值：无
- 描述：登录的ID,该字符串由用户登录后返回，类似session信息

####示例代码

datacloud.userLogout('eOU5DONp99HgGjMOz50EOOMiBUDaoQ')


###**4.发送验证邮件**

验证邮箱<br>
verifyEmail(attr)

####参数
attr

- 类型：JSON对象
- 默认值：无
- 描述：username 待邮件验证的用户名, email 邮件的发送地址, language 发送邮件的语言 

####示例代码

datacloud.verifyEmail({"username":"apicloud","email":"id@apicloud.com","language":"zh_CN"})


###**5.密码重置**

密码重置
resetRequest(attr)

####参数
attr

- 类型：JSON对象
- 默认值：无
- 描述：username 待邮件验证的用户名, email 邮件的发送地址, language 发送邮件的语言

####示例代码

datacloud.resetRequest({"username":"apicloud","email":"id@apicloud.com","language":"zh_CN"})


###**6.获取用户信息**

获取用户信息,如果用户设定的权限为"仅登录状态有此权限"，则authorization必须输入有效值.<br>
getUserInfo(userId,authorization)

####参数

userId

- 类型：字符串
- 默认值：无
- 描述：用户Id

authorization

- 类型：字符串
- 默认值：空
- 描述：登录后的session信息

####示例代码

datacloud.getUserInfo('55796f23dfc407df41432f94')


###**7.更改用户信息**

向对象插入一条数据<br>
updateUserInfo(attr)

####参数

attr

- 类型：JSON对象
- 默认值：无
- 描述：待更改的键值对信息

####示例代码

datacloud.updateUserInfo({'userId':'55796f23dfcdf41432f94','address':'Beijing'})


###**8.删除用户**

删除用户<br>
deleteUser(userId,authorization)

####参数
userId

- 类型：字符串
- 默认值：无
- 描述：对象名称

authorization

- 类型：字符串
- 默认值：空
- 描述：登录后的session信息

####示例代码

datacloud.deleteUser('55796f23dfc407df41432f94')

<br>

##**角色**

###**1.创建角色**

创建以个角色<br>
createRole(attr)

####参数
attr

- 类型：JSON对象
- 默认值：无
- 描述：待插入角色的键值对

####示例代码

createRole({'name':'manager','description':'desc'});


###**2.获取角色**
获取指定id的角色信息<br>
getRole(id)

Id

- 类型：字符串
- 默认值：无
- 描述：对象Id

####示例代码

datacloud.getRole("557966eddfc407df41432f8f")

###**3.更新角色**

更新角色信息
updateRole( id, attr)

####参数
id

- 类型：字符串
- 默认值：无
- 描述：对象id

attr

- 类型：JSON对象
- 默认值：无
- 描述：待更新的的角色信息键值对

####示例代码

datacloud.updateRole('5579748cdfc407df41432f95',{'name':'manager','description':'desc'});

###**4.删除角色**

删除角色表中一条数据<br>
deleteRole(id):

####参数
id

- 类型：字符串
- 默认值：无
- 描述：对象id

####示例代码

datacloud.deleteRole('5579748cdfc407df41432f95');

<br>

##**批量操作**
###**批量操作**

进行批量操作,具体格式信息参考数据云api文档，此处不做详述<br>
batch(attr)

####参数
attr

- 类型：JSON对象
- 默认值：无
- 描述：待批量操作的键值信息

####示例代码

```
datacloud.batch("requests": [
          {
            "method": "POST",
            "path": "/mcm/api/company",
            "body": {
              "name": "apicloud",
              "address": "北京市..."
            }
          },
          {
            "method": "POST",
            "path": "/mcm/api/company",
            "body": {
              "name": "百度",
              "address": "北京市西二旗"
            }
          }
        ])
```
<br>

##**文件上传**
###**文件上传**

文件上传,上传的数据内容会根据设置存到云端并返回一个Http数据地址<br>
upload(filePath, fileType)


####filePath

- 类型：字符串
- 默认值：无
- 描述：文件路径

####fileType

- 类型：String
- 默认值：'application/octet-stream'
- 描述：文件类型，不传则使用默认值

####示例代码

datacloud.upload('E:\\2007119124513598_2.jpg','image/jpeg')

<br>

##**更新操作符**
###**更新操作符**
更新操作符<br>
updateModel(object, id, params)

####参数
object

- 类型：字符串
- 默认值：无
- 描述：对象名称

id

- 类型：字符串
- 默认值：无
- 描述：待操作的数据id

params

- 类型：JSON对象
- 默认值：无
- 描述：待更新的域信息，支持更新操作符，具体操作符信息见数据云api文档

####示例代码

datacloud.updateModel("company", "5579748cdfc407df41432f95", {sku: "abc123",
  quantity: 10})

<br>

##**条件查询操作**
```
支持fields、limit、order、skip、where、include、includefilter等操作符设置，相关参数设置请参考[云api文档](http://docs.apicloud.com/%E4%BA%91API/data-cloud-api#6)
```
###**条件查询操作**

条件数据查询
doFilterSearch(object, filter)


####参数
object

- 类型：字符串
- 默认值：无
- 描述：对象名称

filter

- 类型：字符串
- 默认值：无
- 描述：条件查询信息

####示例代码

datacloud.doFilterSearch("company","filter={"where":{"id":1234}}")
