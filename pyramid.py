floors = 4
h = 2*floors-1
for i in range (1, 2*floors,2):
    print('{:^{}}'.format('*'*i,h))
