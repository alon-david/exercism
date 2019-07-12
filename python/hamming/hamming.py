def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError('Strands length must be equal.')

    sum = 0
    for a, b in zip(strand_a, strand_b):
        if a != b:
            sum += 1

    return sum
