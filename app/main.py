#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
import web_manager
import analysis_manager
import url_manager
import dedecms_manager

if __name__ == '__main__':
	# ����ģ��
	web_manager = web_manager.web_manager()
	analysis_manager = analysis_manager.analysis_manager()
	url_manager = url_manager.url_manager()
	DedeCMS = dedecms_manager.DedeCMS()

	# �����ַ
	root_url = 'http://www.qqyewu.com'
	
	# ��ȡ��ǰʱ���
	nowtime = int(time.time())
	
	# ���ÿ������ļ��ʱ��
	dgetime = 5
	
	# ��ǰ������
	runNum = 0
	
	# ������������ *=���޴�
	runMaxNum = 10000
	
	# ѭ�����
	while True:
		runtime = int(time.time())
		
		# �ж��Ƿ��Ѿ�����ÿ�μ��ȴ�ʱ��
		if runtime > (nowtime+dgetime):
			# ��¼���ǵڶ��ٴμ��
			runNum+=1
			
			# ���ñ��μ��ʱ��
			nowtime = int(time.time())
			
			# ��ȡ���Ŀ������
			roothtml = web_manager.get_html(root_url)
			
			# �жϻ�ȡ���Ŀ�������Ƿ�ɹ�
			if roothtml is None:
				print '��%d�μ��:��ȡ����ʧ��' % runNum
				continue
			else:
				print '��%d�μ��:��ȡ���ݳɹ�' % runNum
			# �������Ŀ������
			rootData = analysis_manager.analysis_nowurls(roothtml, root_url)
			# print rootData
			
			# �жϷ�������Ŀ�������Ƿ����������
			if len(rootData['url']) == 0:
				print 'û�л�ȡ��������'
				continue
			elif url_manager.is_notget(rootData['url']) is None:
				print 'û�����µ�������'
				continue
			else:
				geturls = url_manager.is_notget(rootData['url'])
				print geturls
				# break
			# ѭ����ȡ��������ϸ����
			for url in geturls:
				# ��ȡ����ҳ��html
				itemhtml = web_manager.get_html(url)
				# ��������ҳ����
				itemdata = analysis_manager.DetailData(itemhtml, url)
				# ��ӡһ������ҳ����
				print url
				print itemdata['title']
				# print itemdata['body']
				print itemdata
				print ""
				print ""
				# ���ɼ��������ݷ��͵�dedecms
				if DedeCMS.insert(itemdata) is not None:
					# ����ǰ��url���浽�Ѳɼ��б�
					url_manager.add_successUrl(url)
		if runNum > runMaxNum and runMaxNum is not "*":
			break