#regex

import re

text="i am learning python"
pat=r"learning"
search=re.search(pat,text)
if search:
    print("pattern found")
else:
    print("pattern not found:")




