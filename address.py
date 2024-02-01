# working with json in python 
book = {}
book['tom'] = {
'name': 'tom',
'address' : 'india bihar',
'phone' : 9123818375
}

book['bob'] = {
    'name' : 'bob',
    'address':'Bharat, kolkata',
    'phone':987654321

}

import json
s = json.dumps(book)
#print(s)  # instead of printing we will write to a file
with open("D://python learning//book.txt","w") as f:
    f.write(s)

