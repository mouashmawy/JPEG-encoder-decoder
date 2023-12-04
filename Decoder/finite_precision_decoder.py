from fractions import Fraction
def finite_precision_decoder(precision, symbols, encoded_symbols, probabilities):
    # Reconstruct the fractions and ranges as in the encoder
    whole = 2 ** precision
    half = whole / 2
    quarter = whole / 4

    # Compute r, R, c, and d as in the encoder
    r = [p.numerator for p in probabilities]
    R = sum(r)
    c = [0]
    for i in range(1, len(probabilities)):
        c.append(sum(r[0:i]))
    d = [c[i] + r[i] for i in range(len(probabilities))]

    # Initialize the decoder's state
    a = 0
    b = whole
    value = 0

    # Convert the first precision bits to a number
    for i in range(precision):
        value = value * 2 + (encoded_symbols[i] if i < len(encoded_symbols) else 0)

    decoded_symbols = []

    # decoding process
    for i in range(len(encoded_symbols)):
        # Find the symbol corresponding to 'value'
        symbol_index = None
        for i in range(len(symbols)):
            w = b - a
            if a + round(w * c[i] / R) <= value < a + round(w * d[i] / R):
                symbol_index = i
                break

        if symbol_index is None:
            break  # Break if no symbol matches (end of encoding)

        decoded_symbols.append(symbols[symbol_index])

        # Update the range
        w = b - a
        b = a + round(w * d[symbol_index] / R)
        a = a + round(w * c[symbol_index] / R)

        # Rescale the range and value as in the encoder
        while True:
            if b < half:
                a = 2 * a
                b = 2 * b
                value = 2 * value + (encoded_symbols.pop(0) if encoded_symbols else 0)
            elif a >= half:
                a = 2 * (a - half)
                b = 2 * (b - half)
                value = 2 * (value - half) + (encoded_symbols.pop(0) if encoded_symbols else 0)
            else:
                break

            if a >= quarter and b < 3 * quarter:
                a = 2 * (a - quarter)
                b = 2 * (b - quarter)
                value = 2 * (value - quarter) + (encoded_symbols.pop(0) if encoded_symbols else 0)

    return decoded_symbols


