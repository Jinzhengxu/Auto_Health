# 健康自动打卡系统
![build](https://img.shields.io/badge/build-passing-brightgreen)
![python3](https://img.shields.io/badge/python-3.6.9-blue)
![bilibili](https://img.shields.io/badge/bilibili-support-ff69b4)

## Change Log
### v1.1.0
+ 针对Linux版本增加自主设定打卡时间
### v1.0.0
+ 通过API实现验证码识别
+ 支持Linux服务器全天运行
+ Shell脚本支持Mac OS X通过corntab或launchctl进行定时
+ 支持多用户打卡模式
+ 邮箱自动提醒是否打卡成功

## 安装与环境
### Linux服务器环境配置
#### 桌面环境配置
首先给服务器安装桌面环境，这里我所使用的系统是Ubuntu 18.04 LTS，后续需要xclip的支持，使用KDE桌面环境的需要自行匹配。
```
sudo apt-get update

apt-get install ubuntu-desktop

reboot #重启
```
#### python3第三方库
在服务器上安装pip3并通过pip3安装我们所需要的库文件:
```
sudo apt install python3-pip

pip3 install selenium

pip3 install schedule

pip3 install pyautogui

pip3 install --upgrade requests
```
#### 配置xclip
```
sudo apt-get install libxss1 libappindicator1 libindicator7
sudo apt-get install python3-tk python3-dev
sudo apt-get install xclip
```
#### 安装Chrome浏览器和chromedriver
这里的Chromedriver需要根据chrome浏览器版本号匹配，chromedriver国内[淘宝镜像源](https://npm.taobao.org/)
```
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb #下载Chrome

sudo dpkg -i google-chrome*.deb    # Might show "errors", fixed by next line   #安装Chrome

sudo apt-get install -f

google-chrome --version      # 查看版本

wget https://npm.taobao.org/mirrors/chromedriver/85.0.4183.83/chromedriver_linux64.zip #下载Chromedriver

unzip chromedriver_linux64.zip

sudo mv chromedriver /usr/bin/ 
```
```
wget https://github.com/Jinzhengxu/Auto_Health/archive/master.zip

unzip master.zip 
```

### Mac OS X环境配置

#### 安装Chromedriver

安装方法请见：

mac: https://www.jianshu.com/p/39716ea15d99

#### 安装python第三方库
```
pip install pyobjc-core

pip install pyobjc

pip3 install selenium

pip3 install pillow

pip3 install pyautogui
```

## 使用
首先下载并解压本repo，进入你所使用的系统文件夹，windows的代码和mac相同。

接下来需要修改`info.py`文件中的API密钥：
```
pd_id = "1256123"     #用户中心页可以查询到pd信息
pd_key = "13123"
app_id = "321236"     #开发者分成用的账号，在开发者中心可以查询到
app_key = "12312"
```
上面的四个密钥需要在[打码平台](http://www.fateadm.com/user_home.php)注册后获得。

修改每天固定的打卡时间，注意一定要按照`HH:MM` 的形式：
```
daka_time= "08:21"
```
然后修改发送打卡信息的邮箱的配置,这些信息一般可以在邮箱的设置中找到:
```
MAIL_USER = "your-mail.com"        # 用于发送通知的邮箱
MAIL_PWD = "your-authorization-code"    # 该邮箱的授权码
```

最后添加打卡人的信息，可以添加多条：
```
# 多用户
users = list()
#users.append(User("id", "password", "email", "province", "city"))
```
比如你在山东省济南市，接受打卡信息的邮箱是11112@qq.com，学号是1111，密码是1224，那就在这个文件中加一句：
```
users.append(User("1111", "1224", "11112@qq.com", "山东省", "济南市"))
```
这里需要特别注意的一点是，省份和城市必须和打卡系统中的完全匹配。

修改完信息后，终端执行就可以了
```
python3 main.py
```
不要关闭终端。

打卡的日志文件会保存在当前文件夹下的`Program-log.txt`文件中。

## License
![GPL](https://img.shields.io/badge/License-GPL-informational)
