def string_reverse(string):
    if type(string) == int:
        return -1
    words = string.split(' ')  
    reverse_string = ' '.join(reversed(words)) 
    return reverse_string