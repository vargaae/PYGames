import random
def get_solution(feladvany, talalatok):
    return ''.join(chr if chr in talalatok else '_' for chr in feladvany)
def run_hangman():
    feladvany = random.choice(["macska", "kutya", "cica", "egér"]).upper()
    talalatok, hibapontok = set(), 0
    
    while hibapontok < 13:
        tipp = input("Mi a tipped?").upper()
        if not tipp or len(tipp) > 1 or not tipp.isalpha():
            print("Próbáld újra")
            continue
        
        if tipp in feladvany:
            talalatok.add(tipp)
            rejtveny = get_solution(feladvany, talalatok)
            print(f'Jó tipp!\n{rejtveny}')
            if rejtveny == feladvany:
                print("Győztél!")
                return
        else:
            hibapontok += 1
            print(f'Rossz tipp - Hibapontok: {hibapontok}')
run_hangman()