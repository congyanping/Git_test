import re 
text = 'This is a text'
pattern=r'\bT\w+'
with_case = re.compile(pattern)
without_case = re.compile(pattern,re.IGNORECASE)
for match in with_case.findall(text):
    print "with_case",match
for match in without_case.findall(text):
    print "without_case",match
print
results = "with_case This,without_case This,without_case text"
