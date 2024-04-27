x,y = map(float,input("Enter the two numbwer(x,y):").split())

if x>0 and y>0:
    print(f"the (x,y) point in first quadrant ");
elif x<0 and y>0:
    print(f"the (x,y)point is second quadrant ");
elif x<0 and y<0:
    print(f"the (x,y) point is third quadrant ");
elif x>0 and y<0:
    print(f"the (x,y) point is fourth quadrant ");
elif x==0 and y==0:
    print(f"the point on the origin ");
else:
    print(f"the (x,y) point is on x axis or y axis  ");

    
    
    