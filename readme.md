### 图书馆选座系统

#### Preview
[http://occup.suntangji.me](http://occup.suntangji.me)

#### 功能
- 普通用户

1. 注册
2. 登录
3. 查看座位信息
4. 选座
5. 暂离
6. 离开
7. 查看帮助
8. 反馈
9. 查看公告
10. 查看我的选座信息
11. 退出登录

- 管理员 

1. 登录
2. 查看选座情况
3. 清空所有座位
4. 闭馆/取消闭馆
5. 退出登录
6. 查看反馈
7. 发布公告

#### 使用的语言和库
- Python2
- Flask
- jQuery 
- Bootstrap

#### 安装
0. 下载代码
``` shell
git clone git@github.com:suntangji/occup.git
```
1. 新建虚拟环境
``` shell
pip install virtualenv
virtualenv venv
```
2. 激活虚拟环境
``` shell
venv/Scripts/activate(windows)
. venv/bin/activate(Linux)
``
3. 安装依赖
``` shell
pip install -r requirements.txt
```
4. 修改配置文件config.py
修改数据库配置为你的数据库

5. 初始化数据库
执行init_db.py
6. 运行
执行server.py

