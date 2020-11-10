numero1  =  int ( input ( "digite um número:" ))
numero2  =  int ( input ( "digite o 2° número:" ))
numero3  =  int ( input ( "digite o 3° número:" ))
numero4  =  int ( input ( "digite o 4° número:" ))
numero5  =  int ( input ( "digite o 5° número:" ))
lista  = [ numero1 , numero2 , numero3 , numero4 , numero5 ]
maiores  = [ i  for  i  in  lista  if  i  >=  10 ]
print ( "Os números maiores que 10 são:" , maiores) 