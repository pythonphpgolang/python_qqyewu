#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
import web_manager
import analysis_manager
import url_manager
import diymysql_manager

if __name__ == '__main__':
	web_manager = web_manager.web_manager()
	analysis_manager = analysis_manager.analysis_manager()
	url_manager = url_manager.url_manager()
	DIyMysqlDB = diymysql_manager.DIyMysqlDB()

	root_url = 'http://www.qqyewu.com'
	
	nowtime = int(time.time())
	
	dgetime = 5
	
	runNum = 0
	
	runMaxNum = '*'
	
	while True:
		runtime = int(time.time())
		
		if runtime > (nowtime+dgetime):
			runNum+=1
			nowtime = int(time.time())
			roothtml = web_manager.get_html(root_url)
			if roothtml is None:
				print '��%d�μ��:��ȡ����ʧ��' % runNum
				print ""
				continue
			else:
				print '��%d�μ��:��ȡ���ݳɹ�' % runNum
			rootData = analysis_manager.analysis_nowurls(roothtml, root_url)
			
			if len(rootData['url']) == 0:
				print 'û�л�ȡ��������'
				print ""
				continue
			elif url_manager.is_notget(rootData['url']) is None:
				print 'û�����µ�������'
				print ""
				continue
			else:
				print '��������'
				geturls = url_manager.is_notget(rootData['url'])
			successNum = 0
			for url in geturls:
				itemhtml = web_manager.get_html(url)
				itemdata = analysis_manager.DetailData(itemhtml, url)
				try:
					downloader = itemdata['downloader']
				except Exception as e:
					downloader = ''
				if DIyMysqlDB.addArticle(itemdata['catyname'], itemdata['title'], itemdata['body'], downloader) is not None:
					url_manager.add_successUrl(url)
					print 'д�� %s �����ݳɹ�' % url
				else:
					print 'д�� %s ������ʧ��' % url
		if runNum > runMaxNum and runMaxNum is not "*":
			print '������'
			break