# Naam van de student  
# Studentnummer  
# Doel van het programma: Wisselgeld teruggeven met zo min mogelijk munten  

# Muntsoorten in centen (inclusief 1, 2 en 5 euro munten)  
muntwaarden = [500, 200, 100, 50, 20, 10, 5, 2, 1]  

# Vraag om het te betalen bedrag en het betaalde bedrag  
te_betalen = int(float(input('Bedrag om te betalen (in euro): ')) * 100)  
betaald = int(float(input('Betaald bedrag (in euro): ')) * 100)  

# Bereken het wisselgeld  
wisselgeld = betaald - te_betalen  

# Lijst om bij te houden hoeveel munten er worden teruggegeven  
munten_terug = {munt: 0 for munt in muntwaarden}  

# Controleer of er genoeg is betaald  
if wisselgeld < 0:  
    print("Je hebt te weinig betaald. Betaal het juiste bedrag.")  
else:  
    # Wisselgeld teruggeven met zo min mogelijk munten  
    while wisselgeld > 0 and muntwaarden:  
        munt = muntwaarden.pop(0)  # Pak de grootste munt die nog over is  
        aantal_munten = wisselgeld // munt  # Hoeveel van deze munt kunnen we geven?  

        if aantal_munten > 0:  
            print(f'Geef maximaal {aantal_munten} munten van {munt} cent.')  
            munten_gegeven = int(input(f'Hoeveel munten van {munt} cent geef je terug? '))  

            # Bewaar het aantal teruggegeven munten  
            munten_terug[munt] += munten_gegeven  
            wisselgeld -= munten_gegeven * munt  

    # Controleer of alles is teruggegeven  
    if wisselgeld > 0:  
        print(f'Niet genoeg wisselgeld teruggegeven: {wisselgeld} cent over.')  
    else:  
        print('Wisselgeld correct teruggegeven.')  

    # Print een overzicht van de teruggegeven munten  
    print("\nOverzicht teruggegeven munten:")  
    for munt, aantal in munten_terug.items():  
        if aantal > 0:  
            print(f'{aantal} munten van {munt} cent')  
