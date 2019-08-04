def pana(st):
    stlo=st.lower()
    dic={'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0,}
    for word in st:
        if word=='a':
            dic['a']=1
            continue
        if word=='b':
            dic['b']=1
            continue
        if word=='c':
            dic['c']=1
            continue
        if word=='d':
            dic['d']=1
            continue
        if word=='e':
            dic['e']=1
            continue
        if word=='f':
            dic['f']=1
            continue
        if word=='g':
            dic['g']=1
            continue
        if word=='h':
            dic['h']=1
            continue
        if word=='i':
            dic['i']=1
            continue
        if word=='j':
            dic['j']=1
            continue
        if word=='k':
            dic['k']=1
            continue
        if word=='l':
            dic['l']=1
            continue
        if word=='m':
            dic['m']=1
            continue
        if word=='n':
            dic['n']=1
            continue
        if word=='o':
            dic['o']=1
            continue
        if word=='p':
            dic['p']=1
            continue
        if word=='q':
            dic['q']=1
            continue
        if word=='r':
            dic['r']=1
            continue
        if word=='s':
            dic['s']=1
            continue
        if word=='t':
            dic['t']=1
            continue
        if word=='u':
            dic['u']=1
            continue
        if word=='v':
            dic['v']=1
            continue
        if word=='w':
            dic['w']=1
            continue
        if word=='x':
            dic['x']=1
            continue
        if word=='y':
            dic['y']=1
            continue
        if word=='z':
            dic['z']=1
            continue
    check_list=dic.values()
    for x in check_list:
        if x != 1:
            return 'Fail'
        else:
            return 'done'
