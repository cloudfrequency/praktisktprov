#Author: Rasmus Lannér
#Date: 2024-09-18

print('Ei23 - genrep praktiskt prov ht24')

while True:
    resistans_input = input('Ange resistorer: ').strip()
    
    if resistans_input:  
        resistans_list = [float(r) for r in resistans_input.split(' ')]
        
        serieresistans = sum(resistans_list)
        parallellresistans = 1/(sum(1/r for r in resistans_list))
   
        print(f'Serieresistans: {serieresistans}')
        print(f'Parallellresistans: {parallellresistans}')
        break

    else: 
        print('Serieresistans: 0')
        print('Parallellresistans: 0')
        break