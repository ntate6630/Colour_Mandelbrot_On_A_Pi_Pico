left_edge = -420
right_edge = 300
top_edge = 300
bottom_edge = -300
x_step = 7
y_step = 15
y0 = 0
x0 = 0
x_x = 0
y_y = 0
x = 0
y = 0
i = 0
the_char = 0
max_iter = 200

y0 = top_edge
while(y0 > bottom_edge):
    x0 = left_edge
    while(x0 < right_edge):
        y = 0
        x = 0
        the_char = ' '
        i = 0
        while(i < max_iter):
            x_x = (x * x) / 200
            y_y = (y * y) / 200
            if(x_x + y_y > 800):
                the_char = 0 + i
                str(the_char) 
                if(i == 1):
                    print(u"\u001b[34m", end='')
                if(i == 2):
                    print(u"\u001b[31m", end='')
                if(i == 3):
                    print(u"\u001b[35m", end='')
                if(i > 3 and i < 5):
                    print(u"\u001b[36m", end='')
                if(i > 5 and i < 9):
                    print(u"\u001b[33m", end='')
                if(i > 9):
                    print(u"\u001b[37m", end='')
                    the_char = "@"
                i = max_iter
            y = x * y / 100 + y0
            x = x_x - y_y + x0
            i = i + 1
        print(the_char, end='')
        x0 = x0 + x_step
    print("\n")
    y0 = y0 - y_step
print(u"\u001b[37m", end='')
                


