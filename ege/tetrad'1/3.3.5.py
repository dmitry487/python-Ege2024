x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
even_indexed = x[::2] 
reversed_even = even_indexed[::-1]

x[::2] = reversed_even 

print(x) 
