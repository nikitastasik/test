s_in = input() 
d = {}
for b in s_in:
    if b in d.keys():
        d[b] += 1
    else:
        d[b] = 1
d_sorted = list(d.items())
d_sorted.sort(key=lambda i: i[1])
d_code = {} 

print(d_sorted)

if len(d_sorted) == 1:
    d_code = {d_sorted[0][0]: '0'}

for i in range(0, len(d_sorted) - 1):
    m1 = d_sorted[0]
    m2 = d_sorted[1]
    s = m1[0] + m2[0]
    k = m1[1] + m2[1]
    print(s, k)
    for b in m1[0]:
        print(b)
        if b in d_code.keys():
            d_code[b] = '0' + d_code[b]
        else:
            d_code[b] = '0'
    for b in m2[0]:
        if b in d_code.keys():
            d_code[b] = '1' + d_code[b]
        else:
            d_code[b] = '1'
    print(d_code)
    d_sorted.remove(m1)
    d_sorted.remove(m2)
    d_sorted.append([s, k])
    print(f'd-SORTED{d_sorted}')
s_prev = ''
if len(s_in) != 0:
    for b in s_in:
        s_out = s_prev + d_code[b]
        s_prev = s_out
if len(s_in) == 0:
    l_out = 0
else:
    l_out = len(s_out)
print(len(d.keys()), l_out)
for x, y in d_code.items():
    print(x, end='')
    print(':', y)
print(s_out)
