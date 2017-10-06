import re
string = open('a.txt').read()
new_str = re.sub('[^a-zA-Z0-9\n\.]', ' ', string)
open('b.txt', 'w').write(new_str)
