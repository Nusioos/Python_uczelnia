def sum_seq(sequence):
    """Suma liczb w sekwencji z dowolnie zagnieżdżonymi listami."""
    total = 0
    for item in sequence:
        if isinstance(item, (list, tuple)):
            total += sum_seq(item)   
        else:
            total += item          
    return total



if __name__ == "__main__":
    print(sum_seq([1, 2, 3]))                      
    print(sum_seq([1, (2, 3), [4, [5, 6]], 7]))    
    print(sum_seq([]))                              
    print(sum_seq([[], [[]], (1,)]))                
    print(sum_seq([1.5, (2, [3.5])]))                