def interval_halving(f,a,b,epsilon):
    delta = b - a
    while delta > epsilon:
        delta = b-a
        x_m = a + delta/2
        y_m = f(x_m)

        x_l = a + delta/4
        y_l = f(x_l)
        x_u = b-delta/4
        y_u = f(x_u)

        if y_l < y_m:
            b = x_m
            x_m = x_l
            y_m = y_l

        elif y_u < y_m:
            a = x_m
            x_m = x_u
            y_m = y_u

        else:
            a = x_l
            b =x_u

    return a,b

def f(x):
    return (x-3)**2 +2

a = 0
b = 6
epsilon = 0.1

result= interval_halving(f,a,b,epsilon)
print("Minimum lies in interval:",result)

