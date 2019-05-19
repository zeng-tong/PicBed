#!/usr/bin/python
# encoding: utf-8
import os
import sys
import time, datetime
from workflow import Workflow3
from qiniu import Auth, put_file, etag
import qiniu.config
# 从PyObjC库的AppKit模块引用NSPasteboard主类，和PNG、TIFF的格式类
from AppKit import NSPasteboard, NSPasteboardTypePNG, NSPasteboardTypeTIFF


def notice(msg, title="notice"):
    ''' notoce message in notification center'''
    os.system('osascript -e \'display notification "%s" with title "%s"\'' % (msg, title))

def get_paste_img_file():
    pb = NSPasteboard.generalPasteboard()  # 获取当前系统剪切板数据
    data_type = pb.types()  # 获取剪切板数据的格式类型
    timestamp = timestamps()
    # 根据剪切板数据类型进行处理
    if any(filter(lambda f: f in data_type, (NSPasteboardTypePNG, NSPasteboardTypeTIFF))):
        data = pb.dataForType_(NSPasteboardTypePNG) if NSPasteboardTypePNG in data_type else pb.dataForType_(NSPasteboardTypeTIFF)
        filepath = '/tmp/%s' % timestamp           # 保存文件的路径
        ret = data.writeToFile_atomically_(filepath, False)    # 将剪切板数据保存为文件
        if ret:   # 判断文件写入是否成功
            return timestamp, filepath, True
        else:
            notice("File temp-save fail💔💔💔") 
    else:
        return "", "", False

def timestamps():
    import time
    return int(round(time.time() * 1000))

def main(wf):
    access_key  = os.getenv('access_key')
    secret_key  = os.getenv('secret_key')
    bucket_name = os.getenv('bucket_name')
    domain      = os.getenv('domain')
    q = Auth(access_key, secret_key)
    fileName, filePath, ok = get_paste_img_file()
    if ok:
        token = q.upload_token(bucket_name, fileName)
        ret, info = put_file(token, fileName, filePath)
        wf.add_item(title=u'🎉🎉🎉',subtitle='Uploaded to %s%d' % (domain, fileName) , arg='![%d](%s%d)' % (fileName, domain, fileName), valid=True)
    else:
        wf.add_item(title=u'😂😂😂',subtitle='No picture in clipboard...') 
    wf.send_feedback()

if __name__ == '__main__':
    wf = Workflow3()
    sys.exit(wf.run(main))