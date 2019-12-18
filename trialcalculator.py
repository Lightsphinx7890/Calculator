que = input('Please enter an operator: ')
if que == 'addition':
    def add_numbs(numb1,numb2):
        return numb1 + numb2
    a1 = add_numbs(5,6)
    print(a1)

if que == 'subtraction':
    def sub_numbs(numb1,numb2):
        return numb1 - numb2
    s1 = sub_numbs(10,4)
    print(s1)

if que == 'division':
    def div_numbs(numb1,numb2):
        return  numb1 / numb2
    d1 = div_numbs(10,5)
    print(d1)

if que == 'multiplication':
    def mult_numbs(numb1,numb2):
        return numb1 * numb2
    m1 = mult_numbs(4,2)
    print(m1)

