import hashlib
db = {
            'michael': 'e10adc3949ba59abbe56e057f20f883e',
            'bob': '878ef96e86145580c38c87f0410ad153',
            'alice': '99b1c2188db85afee403b1536010c2c9'
                    }
def login(usr,pwd):
    pwd = str(pwd)
    pwd1 = hashlib.md5()
    pwd1.update(pwd.encode('utf-8'))
    result = pwd1.hexdigest()
    for k,v in db.iteritems():
        if usr == str(k) and result == str(v):
            return "Ture"
        return "False"
f = login("bob",123456)
print f
