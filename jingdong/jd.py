# coding:utf-8
import urllib2, urllib
import json, re

class JD(object):
    def __init__(self, callback, productId):
        self.baseUrl = 'http://sclub.jd.com/comment/productPageComments.action?'
        self.productId = productId
        self.callback = callback
        self.params = {
            'productId': self.productId,
            'score': '0',
            'sortType': '3',
            'pageSize': '10',
            'callback': self.callback
        }
        self.maxPage = -1
        self.pageNum = 0
        self.cnt = 0
        self.errorPage = []

    def getReview(self):
        self.params['page'] = str(self.pageNum)
        url = self.baseUrl + urllib.urlencode(self.params)
        request = urllib2.Request(url)

        try:
            response = urllib2.urlopen(request)
            temp = response.read().decode('gbk')
            temp = temp[len(self.callback)+1:-2]
            res = json.loads(temp)
            if self.maxPage == -1:
                self.maxPage = res['maxPage']
            reviews = []
            for i in range(len(res['comments'])):
                reviews += [(res['comments'][i]['score'], res['comments'][i]['content'])]
            self.cnt += len(res['comments'])
            return reviews

        except urllib2.HTTPError, e:
            print '第%d页数据爬取出错'%self.pageNum
            print e.code
            self.errorPage += [self.pageNum]
            self.pageNum += 1
            return None
        except urllib2.URLError, e:
            print '第%d页数据爬取出错'%self.pageNum
            print e.reason
            self.errorPage += [self.pageNum]
            self.pageNum += 1
            return None
        except UnicodeDecodeError, e:
            print '第%d页数据爬取出错'%self.pageNum
            print e
            self.errorPage += [self.pageNum]
            self.pageNum += 1
            return None

    def start(self, out):
        flag = 0
        with open(out, 'w') as f:
            while True:
                print '正在爬取第%d/%d页'%(self.pageNum, self.maxPage)
                reviews = self.getReview()
                if reviews == None:
                    continue
                print '第%d页爬取成功'%self.pageNum
                print '正在写入第%d/%d页数据'%(self.pageNum, self.maxPage)
                for score, content in reviews:
                    if flag == 0:
                        f.write(str(score)+'\t'+content.encode('utf-8'))
                        flag = 1
                    else:
                        f.write('\n'+str(score)+'\t'+content.encode('utf-8'))
                print '写入第%d页数据完成'%self.pageNum
                self.pageNum += 1
                if self.pageNum >= self.maxPage:
                    print '数据抓取完毕，一共%d条数据'%self.cnt
                    print '错误的页数:%d/%d'%(len(self.errorPage), self.maxPage)
                    print '错误页码:'
                    print self.errorPage
                    break

if __name__ == '__main__':
    #c++primer
    #callback = 'fetchJSON_comment98vv6141'
    #spider = JD(callback,'11306138')
    #out = 'Train/C++Primer.txt'

    #JAVA从入门到精通
    #callback = 'fetchJSON_comment98vv162'
    #spider = JD(callback, '11985075')
    #out = 'Train/JAVA从入门到精通.txt'

    #算法导论
    #callback = 'fetchJSON_comment98vv6156'
    #spider = JD(callback, '11144230')
    #out = 'Train/算法导论.txt'

    #python基础教程
    #callback = 'fetchJSON_comment98vv7175'
    #spider = JD(callback, '11461683')
    #out = 'Train/python基础教程.txt'

    #鸟哥的linux私房菜
    #callback = 'fetchJSON_comment98vv8828'
    #spider = JD(callback, '10064429')
    #out = 'Train/鸟哥的linux私房菜.txt'

    #web设计与前端开发秘籍
    #callback = 'fetchJSON_comment98vv1575'
    #spider = JD(callback, '11775110')
    #out = 'Train/web设计与前端开发秘籍.txt'

    #JavaEE开发的颠覆者
    #callback = 'fetchJSON_comment98vv1097'
    #spider = JD(callback, '11894632')
    #out = 'Train/JavaEE开发的颠覆者.txt'

    #web开发技术丛书
    #callback = 'fetchJSON_comment98vv818'
    #spider = JD(callback, '11462962')
    #out = 'Train/web开发技术丛书.txt'

    #C#入门经典
    #callback = 'fetchJSON_comment98vv148'
    #spider = JD(callback, '12005782')
    #out = 'Train/C#入门经典.txt'

    #python自动化运维
    #callback = 'fetchJSON_comment98vv1179'
    #spider = JD(callback, '11571426')
    #out = 'Train/python自动化运维.txt'

    #SpringMVC学习指南
    #callback = 'fetchJSON_comment98vv1522'
    #spider = JD(callback, '11685552')
    #out = 'Train/SpringMVC学习指南.txt'

    #软件开发视频大讲堂
    #callback = 'fetchJSON_comment98vv505'
    #spider = JD(callback, '11078105')
    #out = 'Train/软件开发视频大讲堂.txt'

    #高性能Linux服务器构建实战
    #callback = 'fetchJSON_comment98vv304'
    #spider = JD(callback, '10898510')
    #out = 'Train/高性能Linux服务器构建实战.txt'

    #callback = 'fetchJSON_comment98vv65'
    #spider = JD(callback, '11219158')
    #out = 'Train/网页设计与制作.txt'

    #Web开发典藏大系
    callback = 'fetchJSON_comment98vv596'
    spider = JD(callback, '11256779')
    out = 'Train/Web开发典藏大系.txt'
    spider.start(out)
