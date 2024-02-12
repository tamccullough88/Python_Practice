def hello():
    print("Hello, User!")


def pack(a, b, c):
    return [a, b, c]

def eat_lunch(food):
    if len(food) == 0:
        print("My lunchbox is empty =(")
    else: 
        for i in range(len(food)):
            if i == 0:
                print(f"first I eat {food[0]}")
            else:
                print(f"Next I eat {food[i]}")


hello()
print(pack("thing 1", "another thing", "and another"))
eat_lunch(["apple", "egg", "brisket", "doughnut"])