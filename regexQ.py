import re
para = '''
Start hjkl sdf hjkl uio jkl; jkl; end
Start hjkl sdzfsgdfb hjkl;fg uio jkl; jkl; end
sffgsdfv hjkl hjkl hjkl uiop hjkl 
'''

pattern = r'^Start.*end$'
exp = re.findall(pattern, para, re.MULTILINE)
print(exp)

txt = 'The big brown ab alia apple fox orange'
p1 = r'^[aeiou].*[^aeiou]$'
e = re.findall(p1, 'ag sd')
print(e)

n = re.findall(r'\b[a-zA-Z]\d+\b', '9zsdf dv z456')
print(n)