# -*- coding: UTF-8 -*-
import sys
from statistic import Statistics, Push
reload(sys)
sys.setdefaultencoding( "utf-8" ) 


############Statistics test#######################
# statistic_cloud = Statistics('A6965066952332','62587239-AD3C-8190-47B4-37DE080D7E9D')
# print 'config content is:'
# print statistic_cloud.printConfigVal()
# print 'getAppStatisticDataById is:'
# print statistic_cloud.getAppStatisticDataById('2015-06-11','2015-06-11')
# print 'getVersionsStatisticDataById is:'
# print statistic_cloud.getVersionsStatisticDataById('2015-06-11','2015-06-11')
# print 'getGeoStatisticDataById is:'
# r = statistic_cloud.getGeoStatisticDataById('2015-06-11','2015-06-11','1.1.25')
# print r['msg'][0]['geoStartupCountResult']
# print 'getDeviceStatisticDataById is:'
# print statistic_cloud.getDeviceStatisticDataById('2015-06-11','2015-06-11')
# print 'getExceptionsStatisticDataById is:'
# print statistic_cloud.getExceptionsStatisticDataById('2015-06-10','2015-06-11')
# print 'getExceptionsDetailByTitle is:'
# print statistic_cloud.getExceptionsDetailByTitle('NullPointerException[com.baidu.mapapi.map.MapView.java,onLayout,-1]')

############push test#######################
push_cloud = Push('A6974706332164','E855BDA3-CD22-C955-04EF-17B45EC5A32A')
print push_cloud.message({ 'title':'你','content':'你好啊哈哈哈哈哈哈哈哈哈哈哈哈哈哈','type':'1','platform':'2'})
print push_cloud.printConfigVal()