import math

def unit_vector(A):
    magnitude = math.sqrt(A[0]**2 + A[1]**2)
    if magnitude == 0:
        raise ValueError("Vektor nol tidak memiliki unit vector.")
    return [A[0] / magnitude, A[1] / magnitude]
