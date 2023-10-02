# Pro 3 dominové kostky
x=1
y=0
x1=3
y1=4
x2=6
y2=7

pole = []

if y == y1 or x == x1 or y==x1 or x ==y1 and x1 == y2 or y1 == x2 or x1==x2 or y1 == y2:
    # 01 12 23
    if y==x+1 and y1==x1+1 and y2==x2+1:
        pole=([x,y],[x1,y1],[x2,y2])
    # 01 21 23
    elif y==x+1 and x1==y1+1 and y2==x2+1:
        pole= ([x,y],[y1,x1],[x2,y2])
    # 01 12 32
    elif y==x+1 and y1==x1+1 and x2==y2+1:
        pole=([x,y],[x1,y1],[y2,x2])
    # 10 12 23
    elif x==y+1 and y1==x1+1 and y2==x2+1:
        pole=([y,x],[x1,y1],[x2,y2])
    # 10 21 23
    elif x==y+1 and x1==y1+1 and y2==x2+1:
        pole=([y,x],[x1,y1],[x2,y2])
    # 10 21 32
    elif x==y+1 and x1==y1+1 and x2==y2+1:
        pole=([y,x],[x1,y1],[x2,y2])

    # x2,y2 nesedí
    elif y == y1 or x == x1 or y==x1 or x==y1:
        # 01 12 
        if y==x+1 and y1==x1+1:
            pole=([x,y],[x1,y1])
        # 01 21
        if y==x+1 and x1==y1+1:
            pole=([x,y],[y1,x1])
        # 10 12
        if x==y+1 and y1==x1+1:
            pole=([y,x],[x1,y1])
        # 10 21
        if x==y+1 and x1==y1+1:
            pole=([y,x],[y1,x1])


    
    
print(pole)