def begin(word: str,count:int):
    first=word[:count]
    print(first)

def end(word: str,count:int):
    last=word[-count:]
    print(last)

word = "Zajecia python odbywaja sie w srody o godzinie 12:00 programuje sie tam czy cos 2"

begin(word,4)
end(word,4)