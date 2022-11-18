import re


def is_a_valid_email(test: str) -> bool:
    pattern = r'[a-zA-z0-9_.+-]+@[a-zA-z0-9-]+\.[a-zA-z0-9-.]+'
    # test = 'mehdimirzaie1378@gmail.com'
    res = re.match(pattern, test)
    return bool(res)

print(is_a_valid_email('mehdimirzaie1378@gmail.com'))
print(is_a_valid_email('email@example.com'))
print(is_a_valid_email('firstname.lastname@example.com'))
print(is_a_valid_email('email@subdomain.example.com'))
print(is_a_valid_email('firstname+lastname@example.com'))
print(is_a_valid_email('email@123.123.123.123'))
print('---------------------------------------')
print(is_a_valid_email('plain address'))
print(is_a_valid_email('#@%^%#$@#$@#.com'))
print(is_a_valid_email(' @example.com'))
print(is_a_valid_email('Joe Smith <email@example.com>'))
print(is_a_valid_email('email.example.com'))
print(is_a_valid_email('email@example@example.com'))
print('---------------------------------------')



# Check if the string starts with "The" and ends with "Spain":
txt = "The rain in Spain"
x = re.search(r"^The.*Spain$", txt)
if x:
    print("YES! We have a match!" )
else:
    print('No match')


print(60 * '-')

txt = """Python was conceived in the late 1980s[38] by Guido van Rossum at Centrum Wiskunde & Informatica (CWI) in
the Netherlands as a successor to ABC programming language, which was inspired by SETL,[39] capable of exception
handling and interfacing with the Amoeba operating system.[9] Its implementation began in December 1989.[40] """
references = re.findall("(\[\d+\])", txt)
print(references)

print(60 * '-')

txt = """Akbar's reign was chronicled extensively by his court historian Abul Fazl in the books Akbarnama and
Ain-i-akbari. Other contemporary sources of Akbar's reign include the works of Badayuni, Shaikhzada Rashidi and
Shaikh Ahmed Sirhindi."""
upper_cases = re.findall("([A-Z]\w*)", txt)
print(upper_cases)


print(60 * '-')

txt = """Non tempora amet 1994-02-24 18:26:25.680292 est. Sed dolor labore ut labore velit porro tempora.
Quisquam
dolor non voluptatem. Numquam quiquia adipisci dolore eius numquam amet voluptatem.
14:39:40.982917 est. Ut tempora quisquam amet 1998-03-16 16:14:16.647591..."""
pattern = r"(\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}(.\d+)?)"
timestamp = re.search(pattern, txt)
print(timestamp)

print(60 * '-')


txt = """Non tempora amet 1994-02-24 18:26:25.680292 est. Sed dolor labore ut labore velit porro tempora.
Quisquam
dolor non voluptatem. Numquam quiquia adipisci dolore eius numquam amet voluptatem.
14:39:40.982917 est. Ut tempora quisquam amet 1998-03-16 16:14:16.647591..."""
pattern = r"(\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}(.\d+)?)"
for ts in re.finditer(pattern, txt):
    print(ts)

"""
.span() returns a tuple containing the start-,and end postion of the match.
.string returns th string passed into the function
.group() returns the part of the where there was a match
.groups() returns all group tuple
groupdict() returns all groups dict
"""

print(60 * '-')


text = '1994-july-21'
pattern = r'(\d{4})\-(\w+)\-(\d{2})'
result = re.match(pattern, text)
print(result)
print(result.span(), type(result.span()))
print(result.string)
print(result.group(2))
print(result.groups())
