#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import os
import shutil
import imghdr
# faker库需要手动安装哦，Google一下就知道怎么安装了
from faker import Faker

# 用户工作目录\\AppData\\Local\\Packages\\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\\LocalState\\Assets
lock_screen_image_path = os.environ['USERPROFILE'] + '\\AppData\\Local\\Packages\\'

print(lock_screen_image_path)

for filename in os.listdir(lock_screen_image_path):
    if filename.find("Microsoft.Windows.ContentDeliveryManager") != -1:
        srcdir = lock_screen_image_path + filename + "\\LocalState\\Assets\\"
        break

# 将图片拷贝到G盘的jpg目录下；
# 程序初步筛选后，自己再手动筛选一下；
# 把好看的图片拷贝到指定目录下
path = 'G:\\jpg\\'
if not os.path.exists(path):
    os.makedirs(path)

i = 1
for file in os.listdir(srcdir):
    srcfile = srcdir + file
    if os.path.isfile(srcfile):
        if os.path.getsize(srcfile) < 100 * 1024:
            continue
        suffix = imghdr.what(srcfile)
        if suffix and suffix != "gif" and suffix != "png":
            shutil.copyfile(srcfile, path + str(i) + "." + suffix)
            i += 1

# 给图片重命名，显得逼格高一些
fake = Faker()
despath = os.environ['USERPROFILE'] + '\\Pictures\\Camera Roll\\'
if os.path.exists(despath):
    for file in os.listdir(despath):
        os.rename(despath + file, despath + fake.name() + '.jpg')


