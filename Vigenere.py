from collections import Counter

from Caesar import caesar, chi_squared

def vigenere(text, key, decrypt=False):
    hasil =""
    i=0
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            k= ord(key[i % len(key)].lower()) - ord('a')
            if decrypt:
                k=-k
            hasil += chr((ord(ch) - base + k) % 26 + base)
            i +=1
        else:
            hasil += ch
    return hasil

enc=vigenere("Attack at dawn", "orange")
print (enc)
print(vigenere(enc,"orange", True))

from collections import Counter

def index_of_coincidence(text):
    n=len(text)
    if n< 2:
        return 0
    return sum(f*(f-1) for f in Counter(text).values())/(n*(n-1)) 