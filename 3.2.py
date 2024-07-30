#([12, 3, 4, 10] == [10, 12, 3, 4])
#[1] == [1]
#[] == []
#[12, 3, 4, 10, 8] == [8, 12, 3, 4, 10]

a = [12, 3, 4, 10, 8]
print(a)
steps = int(input())
for i in range(steps):
    a.insert(0,a.pop())
print(a)