#! -*- coding:utf-8 -*-

#将每一条评论里的换行符去掉，整理成每一条评论一行
import os
import re

pattern = re.compile('^[1-5]\t')
with open('../5A_data/data.txt','r') as f:
	with open('../5A_data/data_1.txt','w') as r:
		r.write(f.readline()[:-1])
		for tmp in f.readlines():
			if pattern.match(tmp):
				r.write('\n'+tmp[:-1])
			else:
				r.write(tmp[:-1])
os.remove('../5A_data/data.txt')
os.rename('../5A_data/data_1.txt','../5A_data/data.txt')
