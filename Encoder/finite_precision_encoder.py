from fractions import Fraction
def finite_precision_encoder(precision,symbols,input,probabilities):
  #precision : number of bits that represent the symbol
  #r : the numerator of the probabilities assuming that they all could be represented as a fraction with the same denumerator
  #R : the sum of all r's
  #c : the lower limit of symbols range
  #d : the upper limits of symbols range

  #setup
  whole=2**precision
  half=whole/2
  quarter=whole/4
  encoded_symbols=[]
  #================================
  r = [p.numerator for p in probabilities]
  R = sum(r)
  c = [0]
  for i in range(1, len(probabilities)):
    c.append(sum(r[0:i]))
  d = [c[i] + r[i] for i in range(len(probabilities))]

  #encoding procedure:
  a=0
  b=whole
  s=0

  for i in range(len(symbols)):
    index_=symbols.index(input[i])
    #calculating the range
    w=b-a
    b=a+round(w*d[index_]/R)
    a=a+round(w*c[index_]/R)

    while(b<half or a> half):
      if(b<half):
        encoded_symbols.append(0)
        for i in range(s):
          encoded_symbols.append(1)

        a=2*a
        b=2*b
        s=0

      elif(a>half):
        encoded_symbols.append(1)
        for i in range(s):
          encoded_symbols.append(0)

        a=2*round(a-half)
        b=2*round(b-half)
        s=0


    while(a>quarter and b<3*quarter ):
      s=s+1
      a=2*round(a-quarter)
      b=2*round(b-quarter)

  s=s+1
  if(a<=quarter):
    encoded_symbols.append(0)
    for i in range(s):
          encoded_symbols.append(1)

  else:
      encoded_symbols.append(1)
      for i in range(s):
        encoded_symbols.append(0)


  return encoded_symbols



