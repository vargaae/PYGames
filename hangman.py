import random
def get_rejtveny(feladvany, talalatok):
    return ''.join(c if c in talalatok else '_' for c in feladvany)
def getFeladvany():
    feladvany = random.choice(["macska", "kutya", "cica", "egér"]).upper()
    talalatok, hibapontok = set(), 0
    
    while hibapontok < 13:
        tipp = input("Mi a tipped?").upper()
        if not tipp or not tipp.isalpha():
            print("Próbáld újra")
            continue
        
        if tipp in feladvany:
            talalatok.add(tipp)
            rejtveny = get_rejtveny(feladvany, talalatok)
            print(f'Jó tipp!\n{rejtveny}')
            if rejtveny == feladvany:
                print("Győztél!")
                return
        else:
            hibapontok += 1
            print(f'Rossz tipp - Hibapontok: {hibapontok}')
getFeladvany()