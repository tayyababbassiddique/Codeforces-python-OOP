# Give a number in input check if it is even and half of of your input is also even. 
# If theese all conditions are true print YES else print NO

class Tayyab:
    def Watermelon(self, w):
        if w % 2 == 0 and w > 3:
            return "Yes"
        return "No"


Object = Tayyab()

w = int(input())
print(Object.watermelon(w))
