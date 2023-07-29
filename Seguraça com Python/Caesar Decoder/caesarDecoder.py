# Basic Caesar Cipher based decoder and encoder functions I've made for a ctf game.
# They only work keys bigger than -30 and less than 30. Numbers must be writen in cursive.
# Each letter have a limit of what key value can be used. So, to don't have issues, I recommend using
# keys with values from -20 to 20. Higher values can generate errors.

def caesarDecoder(string, key):
    try:
        alphabet = ['a', 'b', 'c', 'd',
                    'e', 'f', 'g', 'h',
                    'i', 'j', 'k', 'l',
                    'm', 'n', 'o', 'p',
                    'q', 'r', 's', 't',
                    'u', 'v', 'w', 'x', 'y', 'z']
        string = string.lower()
        aux = []
        try:
            for i in string:
                char = alphabet.index(i)
                index = char + (-key)
                if index > 25:
                    index = index - 26
                aux.append(alphabet[index])
            res = ''.join(aux)
        except IndexError:
            if key < 0:
                return f'Key {key} too low'
            else:
                return f'Key {key} too high'
    except ValueError:
        return "First paramater should be string and second an integer."
    except TypeError:
        return "First paramater should be string and second an integer."
    except AttributeError:
        return "First paramater should be string and second an integer."
    return res


def caesarEncoder(string, key):
    alphabet = ['a', 'b', 'c', 'd',
                'e', 'f', 'g', 'h',
                'i', 'j', 'k', 'l',
                'm', 'n', 'o', 'p',
                'q', 'r', 's', 't',
                'u', 'v', 'w', 'x', 'y', 'z']
    string = string.lower()
    aux = []
    try:
        try:
            for i in string:
                char = alphabet.index(i)
                index = char + key
                if index > 25:
                    index = index - 26
                aux.append(alphabet[index])
            res = ''.join(aux)
        except IndexError:
            if key < 0:
                return f'Key {key} too low'
            else:
                return f'Key {key} too high'
    except ValueError:
        return "First paramater should be string and second an integer."
    except TypeError:
        return "First paramater should be string and second an integer."
    except AttributeError:
        return "First paramater should be string and second an integer."
    return res