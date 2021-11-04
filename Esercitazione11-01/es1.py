def isPalyndrome(str: str):
    newStr = str.lower().replace(' ', '')
    if len(newStr) <= 0:
        return True
    if newStr[0] == newStr[len(newStr)-1]:
        return isPalyndrome(newStr[1:len(newStr)-1])
    else:
        return False

def main():
    print(isPalyndrome("was it a car or a cat i saw"))
    print(isPalyndrome("kjjk"))
    print(isPalyndrome("ifdsfdsfdgggfksojncushcuidbsyuefiaisda"))
main()