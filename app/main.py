#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
import web_manager
import analysis_manager
import url_manager
import dedecms_manager

if __name__ == '__main__':
	web_manager = web_manager.web_manager()
	analysis_manager = analysis_manager.analysis_manager()
	url_manager = url_manager.url_manager()
	DedeCMS = dedecms_manager.DedeCMS()

	root_url = 'http://www.qqyewu.com'
	
	nowtime = int(time.time())
	
	dgetime = 5
	
	runNum = 0
	
	runMaxNum = 10
	
	while True:
		runtime = int(time.time())
		
		if runtime > (nowtime+dgetime):
			runNum+=1
			nowtime = int(time.time())
			roothtml = web_manager.get_html(root_url)
			if roothtml is None:
				print '��%d�μ��:��ȡ����ʧ��' % runNum
				continue
			else:
				print '��%d�μ��:��ȡ���ݳɹ�' % runNum
			rootData = analysis_manager.analysis_nowurls(roothtml, root_url)
			
			if len(rootData['url']) == 0:
				print 'û�л�ȡ��������'
				continue
			elif url_manager.is_notget(rootData['url']) is None:
				print 'û�����µ�������'
				continue
			else:
				geturls = url_manager.is_notget(rootData['url'])
			successNum = 0
			for url in geturls:
				itemhtml = web_manager.get_html(url)
				itemdata = analysis_manager.DetailData(itemhtml, url)
				if DedeCMS.insert(itemdata) is not None:
					url_manager.add_successUrl(url)
					successNum+=1
			if successNum:
				if web_manager.updateHtmlCache(time.strftime('%Y-%m-%d', time.localtime())):
					print "DEDECMS������³ɹ�"
				else:
					print "DEDECMS�������ʧ��"
		if runNum > runMaxNum and runMaxNum is not "*":
			print '������'
			break