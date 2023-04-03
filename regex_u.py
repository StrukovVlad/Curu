# import re
#
#
# def maskify(s):
#     return re.sub('.','@', s[:-4]) + s[-4:] # @@@4567
#     return re.sub('', '@', s[:-4]) + s[-4:] # @1@2@3@4567
#     return re.sub(' ', '@', s[:-4]) + s[-4:]  # 1234567
#
# print(maskify('1234567'))
















# def maskify(cc):
#     s = list(cc)
#     for i in range(0,len(s)-4):
#         s[i] = '#'
#     return ''.join(s)
#
# print(maskify('1234567'))