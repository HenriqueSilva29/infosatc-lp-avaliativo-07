
    

def  conceito ( mediaAluno ): 
    if  media2 <= 5.0  and  media2 >= 0 :
        notaConceito = "D"
    elif  media2 <= 7.0  and  media2 > 5.0 :
        notaConceito = "C"
    elif  media2 < 9.0  and  media2 > 7.0 :
        notaConceito = "B"
    elif  media2 >= 9  and  media2 <= 10 :
        letraConceito = "A"
    return  notaConceito 
media = lambda nota1,nota2: nota1*0.4 + nota2*0.6
for i in range (0,10):
    nota1 = float(input("Qual a sua 1° nota?"))
    nota2 = float(input("Qual a sua 2° nota?"))
    media2 = media(nota1,nota2)
    conceitoo = conceito(media2)
    print("Média do aluno:",media2)
    print("Conceito do aluno:",conceitoo)
