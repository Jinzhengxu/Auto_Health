# 健康自动打卡系统

## Linux服务器环境配置

python版本：3.6.8

sudo apt install python3-pip

wget https://github.com/Jinzhengxu/Auto_Health/archive/master.zip

unzip master.zip 

pip3 install selenium

pip3 install schedule

pip3 install pyautogui

sudo apt-get install libxss1 libappindicator1 libindicator7

sudo apt-get install xclip

wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb

sudo dpkg -i google-chrome*.deb    # Might show "errors", fixed by next line

sudo apt-get install -f

google-chrome --version      # 查看版本

sudo apt-get update

apt-get install ubuntu-desktop #安装桌面软件

reboot #重启

pip3 install --upgrade request

安装chromdriver

进入 [淘宝镜像源](https://npm.taobao.org/) 下载chromdirver

wget https://npm.taobao.org/mirrors/chromedriver/85.0.4183.83/chromedriver_linux64.zip

unzip chromedriver_linux64.zip

sudo mv chromedriver /usr/bin/

## Mac OS X环境配置

### 安装Chromedriver

安装方法请见：

mac: https://www.jianshu.com/p/39716ea15d99

Linux: https://www.jianshu.com/p/86d2227b7e03

Win: https://blog.csdn.net/Hearthougan/article/details/84546130

### 安装selenium
```
 pip3 install selenium
```

### 安装pillow
```
 pip3 install pillow
```

### 安装pyautogui
```
 pip3 install selenium
```
如果你是使用mac，那在安装pyautogui之前还需要这两个模块：
```
pip install pyobjc-core

pip install pyobjc
```
