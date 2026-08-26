# Give a number in input check if it is even and half of of your input is also even. 
# If theese all conditions are true print YES else print NO

class Codeforces_Watermelon:
    def watermelon(self, w):
        if w % 2 == 0 and w > 3:
            return "Yes"
        return "No"


tayyab = Codeforces_Watermelon()

w = int(input())
print(tayyab.watermelon(w))
