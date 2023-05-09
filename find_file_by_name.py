# import os, fnmatch

# def find(pattern, path):
#     res = []
#     for root, dirs, files in os.walk(path):
#         for name in files:
#             if fnmatch.fnmatch(name, pattern):
#                 res.append(os.path.join(root, name))
#     return res

import glob, os

os.chdir(r'C:\Users\mishen\Documents\youtube-downloader-chrome-extension\cache')

pattern = 'on*'

print(glob.glob(pattern))
