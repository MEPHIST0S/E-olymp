#Solution - 1
n = int(input())
sumd = 0

if (n < 0):
    n = abs(n)

while n > 0:
    sumd += n%10
    n = n//10

print(sumd)

#Solution - 2
n = input()
total = 0

for i in n:
    if i != "-":
        total += int(i)

print(total)