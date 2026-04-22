# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
year = input('Em que ano estamos? ')

if int(year) % 4 == 0 and int(year[:2]) / 4  == 5:
     print(f'O ano {year} é bissexto') 
else:
     print(f'O ano {year} não é bissexto')
