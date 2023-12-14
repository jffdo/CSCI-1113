def anonymize(username, domain):
    '''
    Purpose:
        To anonymize emails given username and domain
    Input Parameter(s):
        username: the username
        domain: the domain, such as @gmail.com
    Return Value:
        The anonymized email addresss
    '''
    firstLetter = username[0]
    lastLetter = username[-1]
    newEmail = firstLetter + "*****" + lastLetter + domain
    return newEmail

def list_swap(vals, idx1, idx2):
    '''
    Purpose:
        To swap the given indexes in a given list
    Input Parameter(s):
        vals = the list of values
        idx1 = the first given index to swap with the second given index
        idx2 = the second given index to swap with the first given index
    Return Value:
        The altered list
    '''
    element1 = vals[idx1]
    element2 = vals[idx2]
    vals[idx1] = element2
    vals[idx2] = element1
    return vals

def codename(first, last, codes):
    '''
    Purpose:
        Takes the last letter of the person's name (first and last) and use the given dictionary to return a codename
    Input Parameter(s):
        first = first name
        last = last name
        codes = the given dictionary that contains letters as keys and codewords as values
    Return Value:
        The codename of the name given
    '''
    firstCodeLetter = first[-1]
    lastCodeLetter = last[-1]
    codename = codes[firstCodeLetter] + " " + codes[lastCodeLetter]
    return codename

def cross(u, v):
    '''
    Purpose:
        To compute the cross product of 2 vectors
    Input Parameter(s):
        u = first vector
        v = second vector
    Return Value:
        The cross product of the 2 vectors
    '''
    x = (u[1] * v[2]) - (u[2] * v[1])
    y = (u[2] * v[0]) - (u[0] * v[2])
    z = (u[0] * v[1]) - (u[1] * v[0])
    product = [x, y, z]
    return product
