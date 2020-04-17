'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # TBC
    def inner(w, idx, c):
        length = len(w)
        if idx > length - 2:
            return c
        
        if w[idx] + w[idx+1] == "th":
            return inner(w, idx+1, c+1) 
        else:
            return inner(w, idx+1, c)


    return inner(word, 0, 0)


print(count_th("THtHThth"))

    
    


