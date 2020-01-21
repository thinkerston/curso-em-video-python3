'''Crie um programa em python que testa se o site pudim está acessível pelo
computador usado'''
import requests
try:
    resposta = requests.get('http://pudim.com.br/')
except:
    print('HOUVE UM ERRO AO ACESSAR O SITE PUDIM')
else:
    print('O SITE PUDIM TA FUNFANDO')