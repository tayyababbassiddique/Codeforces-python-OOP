# You will given a string in input.
# If the length of the string is greater than 10, you have to print it's first letter then length of the input minus 2 then last letter of word (without spaces).
# Else print the input exactly.

class Tayyab:
    def way_too_long_words():
        n = int(input())
        for i in range(n):
            a = input()
            if len(a) > 10:
                print(a[0]+str(len(a)-2)+a[-1])
            else:
                print(a)  

Object = Tayyab()
Tayyab.way_too_long_words()
