# 健康自动打卡系统
![build](https://img.shields.io/badge/build-passing-brightgreen)
![python3](https://img.shields.io/badge/python-3.6.9-blue)
![bilibili](https://img.shields.io/badge/bilibili-support-ff69b4)

## Change Log
### v1.0.0
+ 通过API实现验证码识别
+ 支持Linux服务器全天运行
+ Shell脚本支持Mac OS X通过corntab或launchctl进行定时
+ 支持多用户打卡模式

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
wget https://github.com/Jinzhengxu/Auto_Health/archive/master.zip

unzip master.zip 


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

