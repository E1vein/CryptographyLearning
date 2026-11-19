from collections import Counter

def caesar(text, shift):
    result = ""
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result += chr((ord(ch) - base + shift) % 26 + base)
        else:
            result += ch
    return result

#enc = caesar("Hello, World!", 3)
#print (enc)
#print (caesar(enc,-3))

def brute_force_caesar(chipertext):
    for k in range(26):
        print(f"{k:2d}: {caesar(chipertext, -k)}")

#brute_force_caesar("Khoor, Zruog!")

ENGLISH_FREQ = [8.167, 1.492, 2.782, 4.253, 12.702, 2.228, 2.015, 6.094,
                6.966, 0.153, 0.772, 4.025, 2.406, 6.749, 7.507, 1.929,
                0.095, 5.987, 6.327, 9.056, 2.758, 0.978, 2.360, 0.150,
                1.974, 0.074]

def frequency(text):
    letter = [c.upper() for c in text if c.isalpha()]
    total = len(letter)
    cnt = Counter(letter)
    for h, n in cnt.most_common():
        percent = n/total * 100
        print(f"{h}: {n:4d} {percent:5.1f}% {'#' * int(percent)}")
    return cnt

def chi_squared(text):
    letter= [c for c in text.upper() if c.isalpha()]
    n = len(letter)
    if n == 0:
        return float("inf")
    cnt = Counter(letter)
    score = 0
    for i, pct in enumerate(ENGLISH_FREQ):
        expected = pct/100*n
        observed = cnt.get(chr(i+65),0)
        score +=(observed-expected) ** 2 / expected
    return score

def crack_caesar(ciphertext):
    k =  min(range(26), key=lambda k: chi_squared(caesar(ciphertext,-k)))
    return k, caesar(ciphertext, -k)

if __name__ == "__main__":
    enc = caesar("Hello, World!", 3)
    print("Enkripsi :", enc)
    print("Dekripsi :", caesar(enc, -3))
    print("\nBrute force:")
    brute_force_caesar(enc)
    text = "Meet me at the old stone bridge when the sun goes down tonight"
    k, result = crack_caesar(caesar(text, 11))
    print(f"\nCrack: key={k}, result={result}")