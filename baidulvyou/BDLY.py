#! -*- coding:utf-8 -*-
import urllib2
import urllib
import re

class Tool:
	def __init__(self):
		#删除超链接
		self.removeAddr = re.compile('<a.*?>|</a>')

	def replace(self,text):
		text = re.sub(self.removeAddr,'',text)
		return text.strip()

class BDLY:
	#addr：
	def __init__(self,baseUrl, addr):
		self.index = baseUrl+'/'+addr+'/remark/?rn=15&pn='
		self.sub = '&style=hot#remark-container'
		self.pageIndex = 0
		self.rank = 0
		self.remarkNums = 0
		self.tool = Tool()
		self.file = None
	
	def getPage(self, pageNum):
		targetIndex = self.index+str(pageNum)+self.sub
		try:
			request = urllib2.Request(targetIndex)
			response = urllib2.urlopen(request)
			content = response.read().decode('utf-8')
			return content.encode('utf-8')
		except urllib2.URLError, e:
			if hasattr(e, code):
				print e.code
			if hasattr(e, reason):
				print e.reason
			return None
	
	def getRemarkNums(self, content):
		pattern = re.compile('<span class="remark-all-counts">(.*?)</span>',re.S)
		text = re.search(pattern, content)
		if text:
			count = int(text.group(1).decode('utf-8').strip()[:-3])
			return count
		else:
			return None
	
	def getRank(self, content):
		pattern = re.compile('"score":([^"]),',re.S)
		tmpRank = re.findall(pattern, content)
		rank = map(int,tmpRank)
		return rank
	
	def getContent(self, content):
		pattern = re.compile('<div data-remarkid.*?>(.*?)</div>',re.S)
		tmp = re.findall(pattern, content)
		tmpContent = []
		for i in tmp:
			j = self.tool.replace(i)
			tmpContent.append(j)
		return tmpContent
	
	def createFile(self,title):
		self.file = open(title+'.txt','a')
	
	def writeData(self,rank, content):
		for i in range(0,len(content)):
			self.file.write(str(rank[i])+'\t')
			self.file.write(content[i]+'\n')

	def start(self,addr):
		tmpPage = self.getPage(0)
		remarkNums = self.getRemarkNums(tmpPage)
		self.createFile(addr)
		try:
			print "一共有"+str(remarkNums)+"条评论数"
			cur = 0
			while cur<remarkNums:
				print "正在写入第"+str(cur/15)+"页数据"
				text = self.getPage(cur)
				rank = self.getRank(text)
				content = self.getContent(text)
				if len(rank) == len(content):
					self.writeData(rank,content)
					cur += 15
				else:
					print "错误"
					return
			if(remarkNums-(cur-15) != 0):
				print "正在写入第最后一页数据"
				text = self.getPage(cur)
				content = self.getContent(text)
				if len(rank) == len(content):
					self.writeData(rank,content)
					print "写入任务完成"
				else:
					print "错误"
					return
		except IOError, e:
			print e.message
	
if __name__ == '__main__':
	baseUrl = 'http://lvyou.baidu.com/'
	addr = 'shenyangzhiwuyuan'
	spider = BDLY(baseUrl,addr)
	spider.start(addr)
	
