import re
from base64 import b64encode

fname = './assets/7a8a0c288aad2b15e94d84ab4405153f2685734f.js'



def decode_hex():
    def replace_hex(match):
        match = match.group()
        base10 = int(match[1:], 0)
        
        return '(' + str(base10)
    
    with open(fname, 'r', encoding="utf8") as out:
        data = out.read()
        
        data = re.sub('\(0x[0-9a-z]+', replace_hex, data)
    
    with open(fname, 'w+', encoding='utf8') as file:
        file.write(data)
        

def write_base():
    with open(fname, 'rb') as out:
        data = out.read()
        
        with open(fname+'base', 'wb+') as out:
            out.write(b64encode(data))


write_base()
decode_hex()


