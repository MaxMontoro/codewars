def mix(s1, s2):
    abc = 'abcdefghijklmnopqrstuvwxyz'
    one = '1:'
    two = '2:'
    equals = '=:'
    letters = [one + s1.count(letter) * letter
                     if s1.count(letter) > s2.count(letter) 
                        and s1.count(letter) > 1
                     else two + s2.count(letter)*letter
                         if s1.count(letter) != s2.count(letter) and s2.count(letter) > 1
                         else equals + s1.count(letter) * letter
                         for letter in abc if s1.count(letter) > 1 or s2.count(letter) > 1]
    sorted_letters = (sorted(letters, key=lambda x: x[0]))
    result = sorted(sorted_letters, key=lambda x: len(x), reverse=True)
    return "/".join(result)