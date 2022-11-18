import re


text_to_search = """
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be scaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com

321-555-4321
123.555.1234

900-555-4321
800-555-1234
900+555+1234
800|555|1234

mat
bat
pat
fat



Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
"""

sentence = 'Start a sentence and then bring it to an end'

pattern = re.compile(r'coreyms\.com')

matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)


print(60 * '-')


# with open('unique_pass_list.txt', 'r') as f:
#     text = f.read()
#
#
# pass_pattern = re.compile(r'123456')
#
# matches = pass_pattern.finditer(text)
#
# for i in matches:
#     print(i, end='\t')


pattern = re.compile(r'[800|900]+.\d{3}.\d{4}')
result = pattern.findall(text_to_search)
print(result)
