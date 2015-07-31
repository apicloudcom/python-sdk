
##概述

APICloud的 Python SDK 基于python 第三方模块requests创建的工具类,将统计云Api以面向对象的思想加以封装,支持对象化操作,只需要在你的代码中引入Analytics类,便可以轻松完成统计相关api接口的调用,获取符合条件的数据.使用时请使用pip安装requests模块。<br>
SDK只对统计云的API进行封装，返回值不做任何修改，具体返回内容请参照统计云API的相关文档。



###**构造器**


```Python构造器：
Analytics(appId, appKey, url)
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
- 默认值：https://r.apicloud.com/analytics/
- 描述：应用服务器地址，可为空，为空时默认为应用服务器地址，例：https://r.apicloud.com/analytics/

####示例代码

analytics = Analytics(appId, appKey)

<br>
###**获取指定应用ID在某时间范围内的应用统计数据**

```Python
getAppStatisticDataById(startDate, endDate)
```

####参数

startDate

- 类型：字符串
- 默认值：无
- 描述：查询起始时间，格式：YYYY-MM-DD, 如： 2015-01-01

endDate

- 类型：字符串
- 默认值：无
- 描述：查询结束时间，格式：YYYY-MM-DD, 如： 2015-06-01

####示例代码

```
json = analytics.getAppStatisticDataById("2015-01-01", "2015-12-31")
```

<br>
###**获取指定应用ID在某时间范围内各版本的统计数据**

```Python
getVersionsStatisticDataById(startDate, endDate)
```

####参数

startDate

- 类型：字符串
- 默认值：无
- 描述：查询起始时间，格式：YYYY-MM-DD, 如： 2015-01-01

endDate

- 类型：字符串
- 默认值：无
- 描述：查询结束时间，格式：YYYY-MM-DD, 如： 2015-06-01

####示例代码

```
json = analytics.getVersionsStatisticDataById("2015-01-01", "2015-12-31")
```

<br>
###**获取用户指定应用ID在某时间范围内各版本地理分布统计数据**

```Python
getGeoStatisticDataById(startDate, endDate, versionCode)
```

####参数

startDate

- 类型：字符串
- 默认值：无
- 描述：查询起始时间，格式：YYYY-MM-DD, 如： 2015-01-01

endDate

- 类型：字符串
- 默认值：无
- 描述：查询结束时间，格式：YYYY-MM-DD, 如： 2015-06-01

versionCode

- 类型：字符串
- 默认值：无
- 描述：版本号，如： 0.0.1
####示例代码

```Python
json = analytics.getGeoStatisticDataById("2015-01-01", "2015-12-31", "0.0.1")
```

<br>
###**获取用户指定应用ID在某时间范围内各版本设备信息统计数据**

```Python
getDeviceStatisticDataById(startDate, endDate)
```

####参数

startDate

- 类型：字符串
- 默认值：无
- 描述：查询起始时间，格式：YYYY-MM-DD, 如： 2015-01-01

endDate

- 类型：字符串
- 默认值：无
- 描述：查询结束时间，格式：YYYY-MM-DD, 如： 2015-06-01

####示例代码

```
json = analytics.getDeviceStatisticDataById("2015-01-01", "2015-12-31")
```

<br>
###**获取指定应用ID在某时间范围内各版本异常错误统计数据信息**

```Python
getExceptionsStatisticDataById(startDate, endDate)
```

####参数

startDate

- 类型：字符串
- 默认值：无
- 描述：查询起始时间，格式：YYYY-MM-DD, 如： 2015-01-01

endDate

- 类型：字符串
- 默认值：无
- 描述：查询结束时间，格式：YYYY-MM-DD, 如： 2015-06-01

####示例代码

```
json = analytics.getExceptionsStatisticDataById("2015-01-01", "2015-12-31")
```

<br>
###**根据应用异常错误摘要获取异常错误详细信息**

```Python
getExceptionsDetailByTitle("title")
```

####参数

title

- 类型：字符串
- 默认值：无
- 描述：错误摘要信息

####示例代码

```
json = analytics.getExceptionsDetailByTitle("title")
```