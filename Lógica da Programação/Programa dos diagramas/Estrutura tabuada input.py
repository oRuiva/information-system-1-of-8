def tabuada():
    tab = 1
    while tab <= 5:
        i=1
        while i <= 10:
            print (tab,'x',i,'=',tab*i)
            i=i+1
        else:
            tab = tab+1

tabuada()
