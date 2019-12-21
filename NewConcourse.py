import zhihu
from util.conf import Config

Config.init()
Config.CONF.setting('running/style', 0)

# 默认保存到"C:\Users\{user_name}\Documents\zhihuSpider"
# Config.CONF.warehouse(r"")
# zhihu.start()



# #################### demo ####################
# 试爬取2019.12.20知乎热榜第一个问题的第一个回答，默认转成html
# https://www.zhihu.com/question/361816953/answer/942081119
# 爬取结果保存在“桌面\zhihuSpider\answer”

import os
main_path = os.path.join(os.path.expanduser('~'), r'Desktop\zhihuSpider')
# 设置主目录
Config.CON.warehouse(main_path)
# 设置子目录，最终会保存在“桌面\zhihuSpider\answer”
Config.CONF.warehouse('~answer')
zhihu.start(r'https://www.zhihu.com/question/361816953/answer/942081119')
# #################### demo ####################
