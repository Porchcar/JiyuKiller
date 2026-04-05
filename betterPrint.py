from string import printable,ascii_letters,digits,punctuation
from time import sleep
from random import choice

printable_without_flags = ascii_letters+digits+punctuation+" "

def print2dArray(array:list,separator:str=" "):
    def countChinese(s:str):
        return sum(1 for char in s if '\u4e00' <= char <= '\u9fff')

    def countOther(s:str):
        return sum(1 for char in s if not '\u4e00' <= char <= '\u9fff')

    def calcWeight(s:str):
        l = countChinese(s)*2+countOther(s)
        return l
    arrayRows = len(array)
    arrayColumns = 1-1
    for i in array:
        arrayColumns = max(arrayColumns,len(i))
    itemMaxLength = [-1]*arrayColumns
    for i in range(0,arrayColumns):
        for j in range(0,arrayRows):
            try:
                itemMaxLength[i] = max(itemMaxLength[i],calcWeight(array[j][i]))
            except IndexError:
                pass
    for i in range(0,arrayRows):
        for j in range(0,arrayColumns):
            try:
                print(array[i][j]+" "*(itemMaxLength[j]-calcWeight(array[i][j])),end=separator)
            except IndexError:
                pass
        print()

def print2dArray_str(array:list,separator:str=" ",sort:bool=True):
    def countChinese(s:str):
        return sum(1 for char in s if '\u4e00' <= char <= '\u9fff')

    def countOther(s:str):
        return sum(1 for char in s if not '\u4e00' <= char <= '\u9fff')

    def calcWeight(s:str):
        l = countChinese(s)*2+countOther(s)
        return l
    output = ""
    arrayRows = len(array)
    arrayColumns = 1-1
    for i in array:
        arrayColumns = max(arrayColumns,len(i))
    itemMaxLength = [-1]*arrayColumns
    for i in range(0,arrayColumns):
        for j in range(0,arrayRows):
            try:
                itemMaxLength[i] = max(itemMaxLength[i],calcWeight(array[j][i]))
            except IndexError:
                pass
    for i in range(0,arrayRows):
        for j in range(0,arrayColumns):
            try:
                output += array[i][j]+" "*(itemMaxLength[j]-calcWeight(array[i][j]))
                output += separator
            except IndexError:
                pass
        output += "\n"
    return output

def print_inputLike(key:str="",string:str=""):
    currentPrint = ""
    for i in string:
        for j in printable_without_flags:
            showValue = currentPrint+j
            print(key+showValue,end="\r")
            sleep(0.005)
            if i==j:
                currentPrint += j
                break
    print(key+string)

def randomString(length:int):
    return "".join([choice(printable_without_flags) for _ in range(length)])

if __name__ == "__main__":
    # print2dArray([["123","4567三","89101"],
    #               ["111111111111111111111你好","22222","3333"]])
    print_inputLike("Generating licence key1...",randomString(20))