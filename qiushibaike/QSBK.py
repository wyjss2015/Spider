#! -*- coding:utf-8 -*-
import urllib2
import urllib
import re

class QSBK:
	def __init__(self):
		self.pageIndex = 1
		self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
		self.headers = {'User-Agent':self.user_agent}
		self.enable = True

	def getStory(self, pageIndex):
		index = 'http://www.qiushibaike.com/hot/page/%s/?s=4881770'%str(pageIndex)
		request = urllib2.Request(index, headers = self.headers)
		try:
			response = urllib2.urlopen(request)
			content = response.read().decode('utf-8')
			pattern = re.compile('<div class="article.*?<h2>(.*?)</h2>.*?'+'<div.*?content">(.*?)</div>.*?'+'<i.*?number">(.*?)</i>', re.S)
			tmpStory = []
			ab = pattern.findall(content)
			for i in ab:
				replaceBR = re.compile('<br/>')
				text = replaceBR.sub('\n', i[1])
				tmpStory.append([i[0].strip(), text.strip(),i[2].strip()])
			return tmpStory
		except urllib2.URLError, e:
			if hasattr(e,code):
				print e.code
			if hasattr(e, reason):
				print u"错误原因："+e.reason
			return None
	
	def start(self):
		while self.enable:
			userIn = raw_input("加载按回车，退出按Q：")
			if userIn=="Q":
				self.enable = False
				return
			tmpStory = self.getStory(self.pageIndex)
			if tmpStory:
				print "第%s页\n"%str(self.pageIndex)
				for i in tmpStory:
					print i[0]+'\n'+i[1]+'\n'+i[2]+'\n'
				self.pageIndex += 1
	
if __name__ == '__main__':
	spider = QSBK()
	spider.start()
