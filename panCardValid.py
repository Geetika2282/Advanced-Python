import re

txt = 'ABCDE1234L hjkl yuio GHJKW7561J'
pattern = r'\b[A-Z]{5}\d{4}[A-Z]{1}\b'
selected = re.findall(pattern, txt)
print(selected)

