# REGEX: Regular Expression
# ==============================

# from ctypes import addressof


# (\d{1, 3})(\.)(\d{1, 3})(\.)(\d{1, 3})(\.)(\d{1, 3}): IP address
# -> 11.2.1.2
# -> 127.0.0.1

# (\d{4})[\.\-\/](\d{2})[\.\-\/](\d{2}): Date
# -> 1922-02-02
# -> 1340/02/01

# (www.)?([\w\-]+\.)?([\w\-]+)\.([\w\-]{2,})(\/.*)?: ?
import re

passage = '''hello everybody 12345
54231'''

pattern = re.compile(r'\d{5}')
result1 = pattern.search(passage)  # first occurance
result2 = pattern.finditer(passage)  # iterable all of occurance - span(23, 34) first
result3 = pattern.findall(passage)  # list of all occurance

print(result1, list(result2), result3, sep='\n')

simple_text = """date and time is 2022-08-20 21:35"""
pattern = re.compile(r'(\d{4}-\d{2}-\d{2})\s(\d{2}:\d{2})')
result = pattern.search(simple_text)
print('date:', result.group(1))
print('time:', result.group(2))
print('all:', result.group())
print('all:', result.string)

print('-------------------------------')
print(pattern.sub(r'\2 | \1', simple_text))
# print(pattern.sub(r'####', simple_text))

txt = "2022-08-20 21:35"
pattern = re.compile(r'(?P<date>\d{4}-\d{2}-\d{2})\s(?P<time>\d{2}:\d{2})')
result2 = pattern.match(txt)

print(result2.groupdict())
