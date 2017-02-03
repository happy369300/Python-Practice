# ### calculate the number of english letters, space, numbers, and other charactors

# In a txt file

import re
import pprint

def file_in(in_file):
    f=open(in_file)
    content=f.read()
    
    count={}
    for i in content:
        count[i]=count.setdefault(i,0)
        count[i]+=1
    
    x=content.count(' ')
    y=len(re.findall(r'[a-zA-Z]',content))
    z=len(re.findall(r'[0-9]',content))
    others=len(content)-x-y-z

    pprint.pprint(count)
    f.close()
    print("space:",x,"letters:",y,"numbers:",z,"others:",others)
    print("total:",len(content))

    
file_in('HTMLinput.txt')
