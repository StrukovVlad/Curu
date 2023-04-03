# def func(name, age, a, b, *, key):
#     print(name, age, a, b, key)
#
# if __name__ == "__main__":
#     func('Mike', 17, key = 'test')

# class CaseInsensitiveDict(dict):
#
#      def __getitem__(self, key):
#          return dict.__getitem__(self, key.casefold())
#
#      def __setitem__(self, key, value):
#          return dict.__setitem__(self,key, value)
#
#      def __delitem__(self, key):
#          return dict.__delitem__(self, key)
#
#
# dict = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6}
#
# cas = CaseInsensitiveDict(dict)
#
# print(cas.__setitem__('e',23))

import datetime

today = datetime.datetime.now()

print(f"{today:Today's sate is %d %B, %Y. It's a %A}")

print(str(today))
print(repr(today))

# Today's sate is 02 February, 2023. It's a Thursday
# 2023-02-02 18:49:26.880893
# datetime.datetime(2023, 2, 2, 18, 49, 26, 880893)

