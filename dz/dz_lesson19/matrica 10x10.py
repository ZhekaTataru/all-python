import random
n=int(input("Количество рядков --> "))
m=int(input("Количество столбцов --> "))
A=[[random.randint(1,9) for i in range(m)] for r in range(n)]
print(A)
print("==================================")
for i in A:
    print(i)
print("==================================")    
c=[A[r][i] for r in range(n)for i in range(m)if r==i]
print(f"главная диагональ --> {c}")
print("==================================")
b=[A[0][i] for i in range(m)if i==0]
print(f"индекс 1|1  --> {b}")
b=[A[0][i] for i in range(m)if i==1]
print(f"индекс 1|2  --> {b}")
b=[A[0][i] for i in range(m)if i==2]
print(f"индекс 1|3  --> {b}")
b=[A[0][i] for i in range(m)if i==3]
print(f"индекс 1|4  --> {b}")
b=[A[0][i] for i in range(m)if i==4]
print(f"индекс 1|5  --> {b}")
b=[A[0][i] for i in range(m)if i==5]
print(f"индекс 1|6  --> {b}")
b=[A[0][i] for i in range(m)if i==6]
print(f"индекс 1|7  --> {b}")
b=[A[0][i] for i in range(m)if i==7]
print(f"индекс 1|8  --> {b}")
b=[A[0][i] for i in range(m)if i==8]
print(f"индекс 1|9  --> {b}")
b=[A[0][i] for i in range(m)if i==9]
print(f"индекс 1|10  --> {b}")
b=[A[1][i] for i in range(m)if i==0]
print(f"индекс 2|1  --> {b}")
b=[A[1][i] for i in range(m)if i==1]
print(f"индекс 2|2  --> {b}")
b=[A[1][i] for i in range(m)if i==2]
print(f"индекс 2|3  --> {b}")
b=[A[1][i] for i in range(m)if i==3]
print(f"индекс 2|4  --> {b}")
b=[A[1][i] for i in range(m)if i==4]
print(f"индекс 2|5  --> {b}")
b=[A[1][i] for i in range(m)if i==5]
print(f"индекс 2|6  --> {b}")
b=[A[1][i] for i in range(m)if i==6]
print(f"индекс 2|7  --> {b}")
b=[A[1][i] for i in range(m)if i==7]
print(f"индекс 2|8  --> {b}")
b=[A[1][i] for i in range(m)if i==8]
print(f"индекс 2|9  --> {b}")
b=[A[1][i] for i in range(m)if i==9]
print(f"индекс 2|10  --> {b}")
b=[A[2][i] for i in range(m)if i==0]
print(f"индекс 3|1  --> {b}")
b=[A[2][i] for i in range(m)if i==1]
print(f"индекс 3|2  --> {b}")
b=[A[2][i] for i in range(m)if i==2]
print(f"индекс 3|3  --> {b}")
b=[A[2][i] for i in range(m)if i==3]
print(f"индекс 3|4  --> {b}")
b=[A[2][i] for i in range(m)if i==4]
print(f"индекс 3|5  --> {b}")
b=[A[2][i] for i in range(m)if i==5]
print(f"индекс 3|6  --> {b}")
b=[A[2][i] for i in range(m)if i==6]
print(f"индекс 3|7  --> {b}")
b=[A[2][i] for i in range(m)if i==7]
print(f"индекс 3|8  --> {b}")
b=[A[2][i] for i in range(m)if i==8]
print(f"индекс 3|9  --> {b}")
b=[A[2][i] for i in range(m)if i==9]
print(f"индекс 3|10  --> {b}")
b=[A[3][i] for i in range(m)if i==0]
print(f"индекс 4|1  --> {b}")
b=[A[3][i] for i in range(m)if i==1]
print(f"индекс 4|2  --> {b}")
b=[A[3][i] for i in range(m)if i==2]
print(f"индекс 4|3  --> {b}")
b=[A[3][i] for i in range(m)if i==3]
print(f"индекс 4|4  --> {b}")
b=[A[3][i] for i in range(m)if i==4]
print(f"индекс 4|5  --> {b}")
b=[A[3][i] for i in range(m)if i==5]
print(f"индекс 4|6  --> {b}")
b=[A[3][i] for i in range(m)if i==6]
print(f"индекс 4|7  --> {b}")
b=[A[3][i] for i in range(m)if i==7]
print(f"индекс 4|8  --> {b}")
b=[A[3][i] for i in range(m)if i==8]
print(f"индекс 4|9  --> {b}")
b=[A[3][i] for i in range(m)if i==9]
print(f"индекс 4|10  --> {b}")
b=[A[4][i] for i in range(m)if i==0]
print(f"индекс 5|1  --> {b}")
b=[A[4][i] for i in range(m)if i==1]
print(f"индекс 5|2  --> {b}")
b=[A[4][i] for i in range(m)if i==2]
print(f"индекс 5|3  --> {b}")
b=[A[4][i] for i in range(m)if i==3]
print(f"индекс 5|4  --> {b}")
b=[A[4][i] for i in range(m)if i==4]
print(f"индекс 5|5  --> {b}")
b=[A[4][i] for i in range(m)if i==5]
print(f"индекс 5|6  --> {b}")
b=[A[4][i] for i in range(m)if i==6]
print(f"индекс 5|7  --> {b}")
b=[A[4][i] for i in range(m)if i==7]
print(f"индекс 5|8  --> {b}")
b=[A[4][i] for i in range(m)if i==8]
print(f"индекс 5|9  --> {b}")
b=[A[4][i] for i in range(m)if i==9]
print(f"индекс 5|10  --> {b}")
b=[A[5][i] for i in range(m)if i==0]
print(f"индекс 6|1  --> {b}")
b=[A[5][i] for i in range(m)if i==1]
print(f"индекс 6|2  --> {b}")
b=[A[5][i] for i in range(m)if i==2]
print(f"индекс 6|3  --> {b}")
b=[A[5][i] for i in range(m)if i==3]
print(f"индекс 6|4  --> {b}")
b=[A[5][i] for i in range(m)if i==4]
print(f"индекс 6|5  --> {b}")
b=[A[5][i] for i in range(m)if i==5]
print(f"индекс 6|6  --> {b}")
b=[A[5][i] for i in range(m)if i==6]
print(f"индекс 6|7  --> {b}")
b=[A[5][i] for i in range(m)if i==7]
print(f"индекс 6|8  --> {b}")
b=[A[5][i] for i in range(m)if i==8]
print(f"индекс 6|9  --> {b}")
b=[A[5][i] for i in range(m)if i==9]
print(f"индекс 6|10  --> {b}")
b=[A[6][i] for i in range(m)if i==0]
print(f"индекс 7|1 --> {b}")
b=[A[6][i] for i in range(m)if i==1]
print(f"индекс 7|2 --> {b}")
b=[A[6][i] for i in range(m)if i==2]
print(f"индекс 7|3  --> {b}")
b=[A[6][i] for i in range(m)if i==3]
print(f"индекс 7|4  --> {b}")
b=[A[6][i] for i in range(m)if i==4]
print(f"индекс 7|5  --> {b}")
b=[A[6][i] for i in range(m)if i==5]
print(f"индекс 7|6  --> {b}")
b=[A[6][i] for i in range(m)if i==6]
print(f"индекс 7|7  --> {b}")
b=[A[6][i] for i in range(m)if i==7]
print(f"индекс 7|8  --> {b}")
b=[A[6][i] for i in range(m)if i==8]
print(f"индекс 7|9  --> {b}")
b=[A[6][i] for i in range(m)if i==9]
print(f"индекс 7|10  --> {b}")
b=[A[7][i] for i in range(m)if i==0]
print(f"индекс 8|1 --> {b}")
b=[A[7][i] for i in range(m)if i==1]
print(f"индекс 8|2  --> {b}")
b=[A[7][i] for i in range(m)if i==2]
print(f"индекс 8|3  --> {b}")
b=[A[7][i] for i in range(m)if i==3]
print(f"индекс 8|4  --> {b}")
b=[A[7][i] for i in range(m)if i==4]
print(f"индекс 8|5  --> {b}")
b=[A[7][i] for i in range(m)if i==5]
print(f"индекс 8|6  --> {b}")
b=[A[7][i] for i in range(m)if i==6]
print(f"индекс 8|7  --> {b}")
b=[A[7][i] for i in range(m)if i==7]
print(f"индекс 8|8  --> {b}")
b=[A[7][i] for i in range(m)if i==8]
print(f"индекс 8|9  --> {b}")
b=[A[7][i] for i in range(m)if i==9]
print(f"индекс 8|10  --> {b}")
b=[A[8][i] for i in range(m)if i==0]
print(f"индекс 9|1 --> {b}")
b=[A[8][i] for i in range(m)if i==1]
print(f"индекс 9|2  --> {b}")
b=[A[8][i] for i in range(m)if i==2]
print(f"индекс 9|3  --> {b}")
b=[A[8][i] for i in range(m)if i==3]
print(f"индекс 9|4  --> {b}")
b=[A[8][i] for i in range(m)if i==4]
print(f"индекс 9|5  --> {b}")
b=[A[8][i] for i in range(m)if i==5]
print(f"индекс 9|6  --> {b}")
b=[A[8][i] for i in range(m)if i==6]
print(f"индекс 9|7  --> {b}")
b=[A[8][i] for i in range(m)if i==7]
print(f"индекс 9|8  --> {b}")
b=[A[8][i] for i in range(m)if i==8]
print(f"индекс 9|9  --> {b}")
b=[A[8][i] for i in range(m)if i==9]
print(f"индекс 9|10  --> {b}")
b=[A[9][i] for i in range(m)if i==0]
print(f"индекс 10|1  --> {b}")
b=[A[9][i] for i in range(m)if i==1]
print(f"индекс 10|2  --> {b}")
b=[A[9][i] for i in range(m)if i==2]
print(f"индекс 10|3  --> {b}")
b=[A[9][i] for i in range(m)if i==3]
print(f"индекс 10|4  --> {b}")
b=[A[9][i] for i in range(m)if i==4]
print(f"индекс 10|5  --> {b}")
b=[A[9][i] for i in range(m)if i==5]
print(f"индекс 10|6  --> {b}")
b=[A[9][i] for i in range(m)if i==6]
print(f"индекс 10|7  --> {b}")
b=[A[9][i] for i in range(m)if i==7]
print(f"индекс 10|8  --> {b}")
b=[A[9][i] for i in range(m)if i==8]
print(f"индекс 10|9  --> {b}")
b=[A[9][i] for i in range(m)if i==9]
print(f"индекс 10|10  --> {b}")
