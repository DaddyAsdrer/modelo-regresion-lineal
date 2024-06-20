import pickle as pkl

modelo = pkl.load(open('regre_modelo.pkl','rb'))

print(f'Los datos del modelo son m = {modelo.m} y b = {modelo.b}')
