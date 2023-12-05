# nps未授权利用脚本

实现原理：开启一个HTTP代理服务器，通过拦截请求添加额外参数实现未授权访问，可像登录后的正常nps操作一致。

注意：python版本大于等于3.10

## 使用方法

- 安装依赖

```
pip install -r reqirements.txt
```
- 启动

```
python nps未授权.py
```

- 浏览器挂上代理：127.0.0.1:9090

- 访问 [mitm.it](http://mitm.it/) 安装证书，选择Other Platforms下载证书，更改der后缀，双击安装，以便支持HTTPS拦截修改。

- 访问目标nps，即可直接免登录操作。
