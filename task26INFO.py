f = open("27888.txt")
a = f.readline()
S = int(a.split()[0])  # Доступный объём
N = int(a.split()[1])  # Число юзеров

A = []
for i in range(N):
    A.append(int(f.readline()))  # Все значение добавляем в массив
A.sort()  # Сортируем

i = 0       # счетчик
count = 0   # Количество юзеров
aMax = 0    # Максимальное колво данных
iMax = 0    # Максимальное занчение счетчика
sum = 0     # Сумма всех добавленных значений
S0 = S      #


while S - A[i] >= 0:
    sum += A[i]
    S -= A[i]
    aMax = A[i]
    count += 1
    iMax = i
    i += 1

S = sum - aMax  # Текущие используемое место на диске

for i in range(iMax, N):  # Пробегаемся по остаткам и добавляем недостающие
    if S + A[i] <= S0:
        aMax = A[i]

print(count, aMax)
