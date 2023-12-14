def cg_ratio(dna):
    '''
    Purpose:
        To find the ratio of dinucleotides that are 'cg' in the given dna strand
    Input Parameter(s):
        dna = a string representing the dna strand
    Return Value:
        a float value representing the ratio of the amount of 'cg' to the total
        amount of dinucleotides
    '''
    newDna = dna.lower()
    nucleotide = 'atcg'
    cgTotal = 0
    dinucleotideTotal = 0
    for base in range(len(newDna)):
        if newDna[base] not in nucleotide:
            print('Invalid DNA Strand')
            return 0.0
        else:
            dinucleotide = newDna[base:base+2]
            if dinucleotide == 'cg':
                cgTotal += 1
                dinucleotideTotal += 1
            elif len(dinucleotide) == 2:
                dinucleotideTotal += 1
    return (cgTotal/dinucleotideTotal)

def mark(dna,codon,frame):
    '''
    Purpose:
        Takes the given dna strand and searches for the given codon.
        The reading starts at the given frame
    Input Parameter(s):
        dna = a string representing the given dna strand
        codon = a string representing the target codon to search for
        frame = a int representing which index to start at
    Return Value:
        a new string in which every occurence of the target codon is capitalized
    '''
    newDna = []
    newDna.append(dna[:frame])
    for base in range(frame,len(dna),3):
        newDna.append(dna[base:base+3])
    for strand in range(len(newDna)):
        if newDna[strand] == codon:
            newDna[strand] = newDna[strand].upper()
    return ''.join(newDna)

def extract_url(html):
    '''
    Purpose:
        Takes a string of html text and returns the url of the string
    Input Parameter(s):
        html = a string of html text
    Return Value:
        a string of the url found in the given html text
    '''
    urlStart = html.find('href="')
    urlEnd = html.find('"', urlStart+6)
    return html[urlStart+6:urlEnd]
