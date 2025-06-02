def sum_of_squares(n):
    sums=0
    for i in range(n+1):
        sums+=(i*i)
    return sums

print(sum_of_squares(6))