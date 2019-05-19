__PicBed__ 是 `MacOS` 下提高 `markdown` 贴图效率的实用小工具。利用 `Alfred3 with PowerPack` 借助七牛云存储图片，并直接将图片 `URL` 放到剪贴板供你便捷实用.

## 直接用
1. 申请七牛云账号, 配置`对象存储`空间.
2. 下载 [pic-to-markdown-format](https://github.com/zeng-tong/PicBed/pictureBed)
3. Alfred 添加环境变量:
```
1. domain      # 七牛云 URL
2. bucket_name # 存储空间名
3. secret_key  # 密钥
4. access_key  # 密钥
```
![1558287557849](http://cdn.sslocal.cn/1558287557849)
## 造轮子
1. 申请七牛云账号, 配置`对象存储`空间.
2. 新建 Alfred workflow,  `Blank workflow` 。进到该`workflow`目录下，新建 Python 脚本.
3. 安装依赖
```sh
pip install --target=. Alfred-Workflow
pip install --target=. qiniu
```
4. Okay, Go Coding
5. Alfred 添加环境变量:
```
1. domain      # 七牛云 URL
2. bucket_name # 存储空间名
3. secret_key  # 密钥
4. access_key  # 密钥
```
6. Reference

- [Alfred WorkFlow API documentation in Python](https://www.deanishe.net/alfred-workflow/api/index.html)
- [PyObjC here for operate clipboard](https://pyobjc.readthedocs.io/en/latest/)
- [Python clipboard brief intro Blog](https://www.jianshu.com/p/91fd58948607)


