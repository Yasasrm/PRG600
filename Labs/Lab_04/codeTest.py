s = "a e 3 io 5\nt 34 c 2.2 i\n4.5 w ae 2 v\n7 7 go 10.1 m\ny o u 13 5 1 \n9 9 9 ye 3 s"
print(s.split())

for i in s.split():
    print(i)

for i in s.split():
    if i.isdigit():
        print(i)

for i in s.split():
    if not i.isdigit():
        print(i)

nl = [int(i) for i in s.split() if i.isdigit()]
print(nl)
print(sum([int(i) for i in s.split() if i.isdigit()]))