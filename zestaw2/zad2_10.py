def funkcja(line:str) -> str:
    word_amount = 0
    if len(line) < 1:
        pass
    compterator=line[0]

    for i in range(1,len(line)):
        if compterator!= ' ' and line[i]== ' ':
            word_amount+=1
        compterator=line[i]

    if line[len(line)-1] == ' ':
        word_amount -= 1
    print("liczba slow to:",word_amount)
    return word_amount


word = "Zajecia python odbywaja sie w srody o godzinie 12:00 programuje sie tam czy cos 2"
funkcja(word)

