def gen_pwds(symbols: str, n: int) -> [str]:
    if n == 0:
        return [""]
    result = []
    for v1 in symbols:
        passwords = gen_pwds(symbols, n - 1)
        for pwd in passwords:
            password = v1 + pwd
            result.append(password)
    return result

#print(gen_pwds("abcd", 3))

def anagrams(txt: str) -> [str]:
    if len(txt) <= 1:
        return [txt]
    
    result = []
    for i, v in enumerate(txt):
        rest = txt[:i] + txt[i+1:]
        partials = anagrams(rest)
        for part in partials:
            anagram = part + v
            result.append(anagram)
    return result

print(anagrams("ciao"))