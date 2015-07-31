
##概述

APICloud的 Python SDK 基于python 第三方模块requests创建的工具类,将推送云Api以面向对象的思想加以封装,支持对象化操作,只需要在你的代码中引入Push类,便可以轻松完成推送相关api接口的调用.使用时请使用pip安装requests模块。<br>
SDK只对推送云的API进行封装，返回值不做任何修改，具体返回内容请参照推送云API的相关文档。



###**构造器**


```Python构造器：
Push(appId, appKey, url)
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
- 默认值：https://p.apicloud.com/api/push/message
- 描述：应用服务器地址，可为空，为空时默认为应用服务器地址，例：https://p.apicloud.com/api/push/message

####示例代码

push = Push(appId, appKey)

<br>
###**推送消息**

```Python
message(payload)
```

####参数
payload为一个Json格式的键值对，推送消息的相关设置在payload中存储，key格式如下：

title:

- 类型：字符串
- 默认值：无
- 描述：消息标题

content:

- 类型：字符串
- 默认值：无
- 描述：消息内容

type:

- 类型：字符串
- 默认值：无
- 描述：消息类型，1:消息 2:通知

platform:

- 类型：字符串
- 默认值：无
- 描述： 消息发送的目标设备平台， 0 全部平台  1 IOS  2 Android

groupName:

- 类型：字符串
- 默认值：无
- 描述：推送组名，多个组用英文逗号隔开.默认:全部组。eg.group1,group2.

userIds:

- 类型：字符串
- 默认值：无
- 描述：推送用户id, 多个用户用英文逗号分隔，eg. user1,user2


####示例代码

```
json = push.message({ 'title':'标题','content':'内容','type':'1','platform':'2'})
```