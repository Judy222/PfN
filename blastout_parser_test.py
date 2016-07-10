# Eva Bueltel, Kerstin Pfeiffer, Judith Umbach
# Blatt12 Aufgabe 1


import sys
#from optparse import OptionParser

def get_name(file):
  for row in file:
    if row[0] is '>': 
      tmp = ''
      for char in row:
        if char is ' ':
          return tmp
        tmp += char

def get_score(file):
  for row in file:
    search_score = ' Score =  '
    if row.startswith(search_score):
      return row[(len(search_score)-1):((len(search_score)+3))]

def get_raw(file):
  for row in file:
    search_score = ' Score =  '
    if row.startswith(search_score):
      for i in range(0, len(row)):
        if row[i] is '(':
          return row[i+1: i+5]

def get_evalue(file):
  for row in file:
    search_score = ' Score =  '
    if row.startswith(search_score):
      for i in range(0, len(row)):
        if row[i] is 'E':
          for j in range(i, len(row)):
            if row[j] is ',':
              return row[i+9: j]  

def get_identities(file):
  for row in file:
    search_ident = ' Identities'
    if row.startswith(search_ident):
      for i in range(0, len(row)):
        if row[i] is 'I':
          for j in range(i, len(row)):
            if row[j] is '/':
              return row[i+13: j]     

def get_positives(file):
  for row in file:
    search_ident = ' Identities'
    if row.startswith(search_ident):
      for i in range(0, len(row)):
        if row[i] is 'P':
          for j in range(i, len(row)):
            if row[j] is '/':
              return row[i+12: j]

def get_gaps(file):
  for row in file:
    search_ident = ' Identities'
    if row.startswith(search_ident):
      for i in range(0, len(row)):
        if row[i] is 'G':
          for j in range(i, len(row)):
            if row[j] is '/':
              return row[i+7: j]

inputfilename = str(sys.argv[1])
inputfile = open(inputfilename)

for lines in inputfile:
  if '>' in lines:
    name = get_name(inputfile)
  elif ' Score =' in lines:
    score = get_score(inputfile)
    raw = get_raw(inputfile)
    evalue = get_evalue(inputfile)
  elif ' Identities' in lines:
    identities = get_identities(inputfile)
    positives = get_positives(inputfile)
    gaps = get_gaps(inputfile)
    print('%s\t%s\t%s\t%s\t%s\t%s\t%s' %(name, score, \
      raw, evalue, identities, positives, gaps))
print(' ')

inputfile.close()


#parser = OptionParser()
#parser.add_option("-r", default=True)