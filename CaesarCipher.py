import string

def cipher(a_string, key):
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    encrypt = ''
    for c in a_string:
        if c in uppercase:
            newindex = (uppercase.index(c) + key) % 26
            encrypt += uppercase[newindex]
        elif c in lowercase:
            newindex = (lowercase.index(c) + key) % 26
            encrypt += lowercase[newindex]
        else: 
            encrypt += c
    return encrypt

s1 = "Learning python"
print(cipher(s1, 3))
    
