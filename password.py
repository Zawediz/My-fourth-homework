def contains_digit(word):
    s = [i for i in range(10)]
    for i in s:
        if str(i) in word:
            return True
    return False


def check(password):
    if (password.__len__() < 8) or ('anna' in password.lower()) or (len(set(password)) < 4):
        return 'weak'
    elif password.islower() or password.isupper() or not contains_digit(password):
        return 'weak'
    else:
        return 'strong'
