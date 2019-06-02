# -*- coding: utf-8 -*-


'''
 Author :'skywalkeryin'
 Date :  2018-07-13
   关键字搜索：
  http://t.yushu.im/v2/book/search?q={}&start={}&count={}
   isbn搜索：
  http://t.yushu.im/v2/book/isbn/{isbn}
   豆瓣api：
  https://api.douban.com/v2/book
'''

from app import create_app

app = create_app()



# CONFIG is the child class of the dict, app.config['DEBUG'] flask 要求全大写
if __name__ == '__main__':  # Only can execute in the entry point(入口文件)
    app.run(host='0.0.0.0', debug=app.config['DEBUG'], port=81, threaded = True)


