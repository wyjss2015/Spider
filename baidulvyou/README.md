#爬虫之[百度旅游](http://lvyou.baidu.com/)
##程序简介
* 爬取指定的旅游景点所有评论

##目录
* 子目录[5A_data](5A_data)中包含已抓取的31个5A旅游景点评论数据
* 子目录[extradata](extradata)中包含其他景点的数据
* 子目录[tool](tool)中是评论数据的格式修正工具，由于抓取时有些评论内容包含若干段落，该工具将评论内容合并成一段，即一行只有一条评论

##操作
将BDLY.py最下方的addr变量赋予希望爬取的目录
* 以东方明珠景点为例
	* 完整网址：http://lvyou.baidu.com/dongfangmingzhu/
	* 赋值 addr = dongfangmingzhu
	* 运行BDLY.py