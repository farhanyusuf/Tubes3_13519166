def kmpString (input_text, kata_penting):
    counter = repeatPatternCounter(kata_penting)

    i = 0
    j = 0
    while (i < len(input_text)):
        if (kata_penting[j]==input_text[i]):
            if (j == len(kata_penting) - 1):
                return True
            i+=1
            j+=1
        elif (j>0):
            j = counter[j-1]
        else:
            i+=1

    return False

def repeatPatternCounter (pattern):
    counter = [0 for i in range (len((pattern)))]

    i = 1
    j = 0
    while (i < len(pattern)):
        if (pattern[j]==pattern[i]):
            counter[i] = j+1
            i+=1
            j+=1
        elif (j>0):
            j = counter[j-1]
        else:
            i+=1
    
    return counter


print(kmpString("hai aku leo", "leo"))