#! -*- coding:utf-8 -*-
import urllib2
import urllib
import re

class Tool:
	def __init__(self):
		#删除图片
		self.removeImg = re.compile('<img.*?>')
		#删除超链接
		self.removeAddr = re.compile('<a.*?>|</a>')
		#替换br
		self.replaceBR = re.compile('<br>+')

	def replace(self,text):
		text = re.sub(self.removeImg,'',text)
		text = re.sub(self.removeAddr,'',text)
		text = re.sub(self.replaceBR,'\n',text)
		return text.strip()

class BDTB:
	#tbcode：贴吧代号 seeLz：是否只看楼主
	def __init__(self,baseUrl, tbcode, seeLz):
		self.index = baseUrl+tbcode+'?see_lz='+str(seeLz)
		self.pageIndex = 1
		self.title = ''
		self.pageNums = 0
		self.tool = Tool()
		self.file = None
	
	def getPage(self, pageNum):
		targetIndex = self.index+'&pn='+str(pageNum)
		try:
			request = urllib2.Request(targetIndex)
			response = urllib2.urlopen(request)
			content = response.read().decode('utf-8')
			return content
		except urllib2.URLError, e:
			if hasattr(e, code):
				print e.code
			if hasattr(e, reason):
				print e.reason
			return None
	
	def getTitle(self, content):
		pattern = re.compile('<h3 class="core_title_txt pull-left text-overflow.*?396px">(.*?)</h3>',re.S)
		text = re.search(pattern, content)
		if text:
			title = text.group(1).strip()
			return title
		else:
			return None
	
	def getPageNums(self, content):
		pattern = re.compile('<li class="l_reply_num".*?<span class="red">(.*?)</span>',re.S)
		tmp = re.search(pattern, content)
		pageNums = int(tmp.group(1).strip())
		return pageNums
	
	def getContent(self, content):
		pattern = re.compile('<div id="post_content_.*?">(.*?)</div>',re.S)
		tmp = re.findall(pattern, content)
		tmpContent = []
		for i in tmp:
			j = '\n'+self.tool.replace(i)+'\n'
			tmpContent.append(j.encode('utf-8'))
		return tmpContent
	
	def createFile(self,title):
		if title is not None:
			self.file = open(title+'.txt','a')
		else:
			self.file = open(u'百度贴吧'+'.txt','a')
	
	def writeData(self, content):
		for i in content:
			self.file.write(i)

	def start(self):
		firstPage = self.getPage(1)
		pageNums = self.getPageNums(firstPage)
		title = self.getTitle(firstPage)
		self.createFile(title)
		try:
			print "帖子一共有"+str(pageNums)+"页"
			for i in range(1,int(pageNums)+1):
				print "正在写入第"+str(i)+"页数据"
				text = self.getPage(i)
				content = self.getContent(text)
				self.writeData(content)
		except IOError, e:
			print e.message
		finally:
			print "写入任务完成"
	
if __name__ == '__main__':
	baseUrl = 'http://tieba.baidu.com/p/'
	#tbCode = '3138733512'
	tbCode = raw_input('请输入帖子代号：')
	#see_Lz = 1
	see_Lz = input("是否只取得楼主发言，是输入1，否输入0：")
	spider = BDTB(baseUrl,tbCode, see_Lz)
	spider.start()
	
