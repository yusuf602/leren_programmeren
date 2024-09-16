print("Denk aan een kaas en beantwoord de vragen met ja of nee.")

vraag = input("Is de kaas geel? (ja/nee): ")

if vraag == 'ja':
    vraag = input("zitten er gaten in? (ja/nee): ")
    
    if vraag == 'ja':
        vraag = input("Is de kaas belachelijk duur? (ja/nee): ")
        
        if vraag == 'ja':
            print("De kaas is Emmentaler.")
        else:
            print("De kaas is Leerdammer.")
    
    else:
        vraag = input("Is de kaas hard als steen? (ja/nee): ")
        
        if vraag == 'ja':
            print("De kaas is Parmigiano Reggiano.")
        else:
            print("De kaas is Goudse kaas.")
            
else:
    vraag = input("Is de kaas blauw van schimmel? (ja/nee): ")
    
    if vraag == 'ja':
        print("De kaas is Bleu de Rochbaron.")
    else:
        vraag = input("Heeft de kaas een korst? (ja/nee): ")
        
        if vraag == 'ja':
            print("De kaas is Camembert.")
        else:
            print("De kaas is Mozzarella.")