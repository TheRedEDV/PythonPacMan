# class Fruit():
    # def __init__(self):
        # self.level = 1
        # self.fruit_table = ["", 
                            # "cherry", "strawbery", 
                            # "peach", "peach", 
                            # "apple", "apple", 
                            # "melon", "melon", 
                            # "flagship", "flagship", 
                            # "bell", "bell",
                            # "key", "key",
                            # "key", "key",
                            # "key", "key",
                            # "key", "key",           ]


    

# a = Fruit()

# a.Display_Fruits()

x = 1
y = 256

while True:
    print(x)
    # 0 =   00000000
    # 255 = 11111111
    if x > 255:
        x = 0
        
    if y > 255:
        y = 0
        
    if y == x:
        break
    
    x += 1