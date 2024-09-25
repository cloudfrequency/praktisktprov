# Author: Rasmus Lannér
# Date: 2024-09-25


while True:
    tabell_input = input('\nVilka tabeller vill du beräkna? ').strip()
    
    tabell_list = [float(m) for m in tabell_input.replace(',', ' ').split()]

    for value in tabell_list:
        print('\n')
        for i in range(1, 11):
            multiplication = value * i
            print(f'{value} * {i} = {multiplication}')     
    break