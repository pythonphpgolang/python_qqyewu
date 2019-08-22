#!/usr/bin/python
# -*- coding: utf-8 -*-
import time,web_manager,analysis_manager

if __name__ == '__main__':
	# ����ģ��
	web_manager = web_manager.web_manager()
	analysis_manager = analysis_manager.analysis_manager()

	# �����ַ
	root_url = 'http://www.qqyewu.com'
	
	# ��ȡ��ǰʱ���
	nowtime = int(time.time())
	
	# ���ÿ������ļ��ʱ��
	dgetime = 0.1
	
	# ��ǰ������
	runNum = 0
	
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
			print rootData
			break
			# �жϷ�������Ŀ�������Ƿ����������
			
			
			# ѭ���ж��Ƿ��Ѿ���ȡ��
			
			
			# ѭ����ȡ��������ϸ����
			
			
			# ��ȡ��ǰ��������ϸ�����е�ָ������
			
			
			# ��¼��ǰ��ȡ��������
			
			
			# ��¼��ǰ��ȡ��������ַ
			
		if runNum > 100:
			break