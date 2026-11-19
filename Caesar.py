def caesar(text, shift):
    hasil = ""
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            hasil += chr((ord(ch) - base + shift) % 26 + base)
        else:
            hasil += ch
    return hasil

enc = caesar("Hello, World!", 3)
print (enc)
print (caesar(enc,-3))

def brute_force_caesar(chipertext):
    for k in range(26):
        print(f"{k:2d}: {caesar(chipertext, -k)}")

brute_force_caesar("Khoor, Zruog!")

from collections import Counter

def hitung_frekuensi(text):
    huruf = [c.upper() for c in text if c.isalpha()]
    total = len(huruf)
    cnt = Counter(huruf)
    for h, n in cnt.most_common():
        persen =n/total*100
        print(f"{h}: {n:4d} {persen: 5.1f}% {'#'* int(persen)}")
    return cnt

ENGLISH_FREQ = [8.167, 1.492, 2.782, 4.253, 12.702, 2.228, 2.015, 6.094,
                6.966, 0.153, 0.772, 4.025, 2.406, 6.749, 7.507, 1.929,
                0.095, 5.987, 6.327, 9.056, 2.758, 0.978, 2.360, 0.150,
                1.974, 0.074]

def chi_squared(text):
    huruf=[c for c in text.upper() if c.isalpha()]
    n=len(huruf)
    if n == 0:
        return float("inf")
    cnt = Counter(huruf)
    skor =0
    for i, pct in enumerate(ENGLISH_FREQ):
        diharapkan = pct/100*n
        teramati = cnt.get(chr(i+65),0)
        skor +=(teramati - diharapkan) ** 2/diharapkan
    return skor

def crack_caesar(ciphertext):
    k=min(range(26), key= lambda k: chi_squared(caesar(ciphertext, -k)))
    return k, caesar(ciphertext, -k)


