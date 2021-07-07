import json
from difflib import get_close_matches

data1 = json.load(open("data.json"))

def translate(w):

    w = w.lower()
    if w in data1:
        return data1[w]

    elif len(get_close_matches(w,data1.keys(),cutoff=0.8))>0:
        print("Did you mean %s instead ? " %(get_close_matches(w,data1.keys(),cutoff=0.8))[0] )
        
        ans = input("press Y if yes ")
        if (ans == "Y" or ans == "y"):
            return data1[(get_close_matches(w,data1.keys(),cutoff=0.8))[0]]
        else:
            return "Word doesnt exist .Please check again"    
    
    else:
        return "Word doesnt exist .Please check again"    

word = input("enter word : ")
#print(translate(word))

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)        
