def hello():
    print("Hello user")


def pack(x,y,z):
    return [x,y,z]

def eat_lunch(food_list):
    if not food_list:  
        print("My lunchbox is empty!")
    else:
        print(f"First I eat {food_list[0]}")
        for food in food_list[1:]:
            print(f"Next I eat {food}")



hello()

print(pack("a","b","c"))
print(pack(1,2,3))

eat_lunch([])
eat_lunch(["sandwich", "apple", "chips"])