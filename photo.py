import urllib.request
import os
import time


def open_url(url):#打开网页
    req = urllib.request.Request(url)#创建一个Request对象
    req.add_header("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36")
    #添加头部请求信息
    response = urllib.request.urlopen(url)
    html = response.read()#read([size])方法从文件当前位置起读取size个字节，若无参数size，则表示读取至文件结束为止，它范围为字符串对象
    return html

def find_first(html):#找到第一个网页
    a = html.find("http://www.win4000.com/wallpaper_detail_")
    b = html.find(".html",a)
    html_url = html[a:b+5]#找到第二个网页
    
    return html_url

def find_html(url,num,folder):
    html = open_url(url).decode("utf_8")
    a = html.find("<div class=\"pic-next-img\"><a href=\"")+35
    b = html.find("\">下一张",a)
    html_url = html[a:b]#找到下一张图片的地址
    c = html.find("pic-large")
    d = html.find(".jpg",c)
    imgs_addrs = html[c+16:d+4]#找到图片的地址
    save_imgs(folder,imgs_addrs)#保存图片
    time.sleep(8)#睡八秒，以防被抓
    
    num -= 1#图片数减一
    while num > 0:
        return find_html(html_url,num,folder)#根据上面获得的下一张图片的地址，重复操作，有点类似递归

def save_imgs(folder,imgs_addrs):
        filename = imgs_addrs.split("/")[-1]#切片获得文件名
        with open(filename,"wb") as f:#以二进制方式打开，结束时自动关闭
            img = open_url(imgs_addrs)
            f.write(img)#写入图片
        
def down_load(folder="bz",num = 1000):
    os.mkdir(folder) #创建一个文件夹
    os.chdir(folder) #切换工作目录到该文件夹
    url = "http://www.win4000.com/zt/huyan.html"#首页地址
    html = open_url(url).decode("utf_8")#以utf_8方式解码
    html_url = find_first(html)
    find_html(html_url,num,folder)
    
if __name__ == "__main__":
    down_load()#调用主函数
    
    
        
        
        
        
    
