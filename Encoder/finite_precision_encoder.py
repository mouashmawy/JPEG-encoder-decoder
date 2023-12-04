from fractions import Fraction
def finite_precision_encoder(precision, symbols, input_symbols, probabilities):
    # Initialize the encoder's state
    whole = 2 ** precision
    half = whole // 2
    quarter = whole // 4

    # Compute r, R, c, and d as in the decoder
    r = [p.numerator for p in probabilities]
    R = sum(r)
    c = [0]
    for i in range(1, len(probabilities)):
        c.append(sum(r[0:i]))
    d = [c[i] + r[i] for i in range(len(probabilities))]

    a = 0
    b = whole
    encoded_bits = []

    # Encoding process
    for symbol in input_symbols:
        # Find the index of the symbol
        symbol_index = symbols.index(symbol)

        # Calculate the new range
        w = b - a
        b = a + (w * d[symbol_index]) // R
        a = a + (w * c[symbol_index]) // R

        # Rescale the range and output bits as necessary
        while True:
            if b < half:
                encoded_bits.append(0)
                a *= 2
                b *= 2
            elif a >= half:
                encoded_bits.append(1)
                a = 2 * (a - half)
                b = 2 * (b - half)
            else:
                break

            if a >= quarter and b < 3 * quarter:
                a = 2 * (a - quarter)
                b = 2 * (b - quarter)

    # Output the remaining bits
    # Check if 'a' is in the lower half or the upper quarter
    if a < quarter:
        encoded_bits.append(0)
        for i in range(precision - len(encoded_bits)):
            encoded_bits.append(1)  # Padding with 1s
    else:
        encoded_bits.append(1)
        for i in range(precision - len(encoded_bits)):
            encoded_bits.append(0)  # Padding with 0s

    return encoded_bits




