  
numero  =  int ( input ( "digite um número:" ))
operacao  = [lambda  x : x ** 2 ,lambda  x : x ** 3 ]
for  i  in  operacao :
    print ( i ( numero ))