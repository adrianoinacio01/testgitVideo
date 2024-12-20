per1 = ''
per2 = ''
per3 = ''
per4 = ''
per5 = ''
culp = 0
while True:
    if per1 != 'sim' and per1 != 'não':
        print('Utilizar sim ou não')
        per1 = str(input('Telefonou para a vítima? ')).strip().lower()
        if per1 == 'sim':
            culp = 1
            print (culp)
    elif True:
         per2 = str(input('Esteve no local do crime? ')).strip().lower()
         if per2 == 'sim':
             culp += 1
             print(culp)
         if per2 != 'sim' and per2 != 'não':
             print('Utilizar sim ou não')
             per2 = str(input('Esteve no local do crime? ')).strip().lower()
             #if per2 == 'sim':
             #    culp += 1
             #    print(culp)
         elif True:
             per3 = str(input('Mora perto da vítima? ')).strip().lower()
             if per3 != 'sim':
                 culp += 1
                 print (culp)
             if per3 != 'sim' and per3 != 'não':
                 print('Utilizar sim ou não')
                 per3 = str(input('Mora perto da vítima? ')).strip().lower()
                elif True:
                    per4 = str(input('Devia para a vítima? ')).strip().lower() 
                    if per4 != 'sim' and per4 != 'não':
                        print('Utilizar sim ou não')
                    per4 = str(input('Devia para a vítima? ')).strip().lower()
                 elif True:
                     per5 = str(input('Já trabalhou com a vítima? ')).strip().lower()
                     if per5 != 'sim' and per5 != 'não':
                         print('Utilizar sim ou não')
                         per5 = str(input('Já trabalhou com a vítima? ')).strip().lower()
                     else:
                         break
                 else:
                     break
             else:
                 break
         else:
             break
    else:
        break

#while True:
#    if per1

#num1 = float(input(' Qual sua nota? '))
#while True:
#    if num1 > 10:
#        num1 = float(input('Número maior que 10. Qual sua nota? '))
#    elif num1 < 0:
#        num1 = float(input('Número maior que 10. Qual sua nota? '))
#    else:
#        print('sua nota é ', num1)
#        break   

# usar matriz
#matx = [
#    [1,2,3,0],
#    [4,5,6,8],
#    [7,8,9,0]
#]
#for linha in matx:
#    for elemento in linha:
#        print(elemento, end=' ')
#    print()

# numerate
#num1 = [23,24,25,26,27]
#soma = 0
#for i in num1:
#    soma += i
#    print(i, soma)

# RANGE() e len()
#ii2 = [1,2,3,4,5,6,7,8,9,10]
#for ii3 in range(len(ii2)):
#   if float(ii2[ii3]) == 0:
#        break
#    else
#        print(float(ii3) / float(ii2[ii3]))
    
#for i in range(-5,2,3):
#    print(i)





# utilização de FOR
#num1 = ['1.1','test','22','23/34']
#for num2 in num1:
#    print('numeros: ', num2)
#num3 ={'Primeiro' : 67, 'Segundo' : 98}
#for num4, num5 in num3.items():
#    print(num4,':',num5)

# while com break
#while num1 < 10:
#    print('numero: ', num1)
#    num1 += 1
#    if num1 == 6:
#        continue
#    print('fim')
    
# uso de while
#while num1 < 10:
#    print(num1)
#    num1 += 1


# rotina de match
#match num1:
#    case 1:
#        print('domingo')
#    case 2:
#        print('segunda-feira')
#    case 3:
#        print('terça-feira')          

# rotina de if elif else
#if num1 > 5:
#   print('é maior que 5')
#elif num1 == 5:
#   print('é igual a 5')
#else:
#    print('é menor que 5')