pop_kindu = int(input('Entrez la population Kindu ici:  '))
pop_boma = int(input('Entrez la population Boma ici:  '))
i = 0
while(pop_kindu > pop_boma):
    pop_kindu = pop_kindu + 30000
    pop_boma = pop_boma + ((pop_boma*2)/100)
    i = i + 1
print("La population de Boma depassera la population de Kindu dans",i,"ans")
