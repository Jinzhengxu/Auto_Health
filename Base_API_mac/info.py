class User:
    uid = ""
    pwd = ""
    email = ""
    province = ""
    city = ""
    def __init__(self, uid, pwd, email, province, city):
        self.uid = uid
        self.pwd = pwd
        self.email = email
        self.province = province
        self.city = city
        
pd_id = "1256123"     #用户中心页可以查询到pd信息
pd_key = "13123"
app_id = "321236"     #开发者分成用的账号，在开发者中心可以查询到
app_key = "12312"

MAIL_USER = "your-mail.com"        # 用于发送通知的邮箱
MAIL_PWD = "your-authorization-code"    # 该邮箱的授权码
# 单用户
UID = "your-id"         # 学号
PWD = "your-password"   # 密码
MAIL_TO = "your-email"  # 接受通知的邮箱
# 多用户
users = list()
#users.append(User("id", "password", "email", "province", "city"))

for user in users:
    print(user.uid)
