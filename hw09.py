def total_hours(fname, employee):
    '''
    Purpose:
        Takes a string with the name of a CSV and string with the name of an
        employee. Then returns the total number of hours the employee worked.
    Input Parameters:
        fname = string representing the name of a csv
        employee = a string representing the name the employee
    Return Value:
        A integer representing the total number of hours worked. If file does
        not exist, the return will be -1.
    '''
    try:
        with open(fname, 'r') as f:
            text = f.readlines()
            hours = 0
            for ln in text:
                lst = ln.split(',')
                if lst[0] == employee:
                    hours += int(lst[1])
        return hours
    except FileNotFoundError:
        return -1

def add_docstring(fname):
    '''
    Purpose:
        Add documentation to functions in the given python file. Returns the
        altered file as docstring_ (given file) and outputs the number of
        functions encountered.
    Input Parameters:
        fname = a string representing the name of the python file
    Return Value:
        A integer representing the total number of functions encountered. If
        file does not exist, the return will be -1.
    '''
    try:
        with open(fname, 'r') as f:
            text = f.readlines()
            numFunction = 0
            newfname = 'docstring_' + fname
            with open(newfname, 'w') as newf:
                for ln in text:
                    if ln[0:3] == 'def':
                        numFunction += 1
                        newf.write(ln)
                        newf.write("    '''\n")
                        newf.write("    Purpose: FILL ME IN\n")
                        newf.write("    Input Parameters: FILL ME IN\n")
                        newf.write("    Return Value: FILL ME IN\n")
                        newf.write("    '''\n")
                    else:
                        newf.write(ln)
        return numFunction
    except FileNotFoundError:
        return -1

def widen_model(fname_in, fname_out):
    '''
    Purpose:
        Reads all the vertices and faces in the given obj file. Then widen the
        obj and save all changes as the second file name.
    Input Parameters:
        fname_in = a string representing the file name
        fname_out = a string representing the file name with the altered obj
    Return Value:
        A integer representing the number of vertices widened. If file does not
        exist, the return will be -1.
    '''
    try:
        with open(fname_in, 'r') as f:
            text = f.readlines()
            vWidened = 0
            with open(fname_out, 'w') as newf:
                for ln in text:
                    if ln[0] == 'v':
                        vWidened += 1
                        vertex = ln.split(' ')
                        vertex[1] = str(float(vertex[1]) * 2)
                        newf.write(' '.join(vertex))
                    else:
                        newf.write(ln)
        return vWidened
    except FileNotFoundError:
        return -1
