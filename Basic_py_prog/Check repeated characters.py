s = str(input('enter one string:'))
l = len(s)
c = []

count = 0
for i in range(l):        #checkng the condition

    if c == s[i]:
        count += 1
    else:
        c = s[i]

if count == 2:
    print('invalid')
else:
    print('valid')
