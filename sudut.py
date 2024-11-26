import math

def sudut_antar_vektor(A, B):
    dot_product = A[0] * B[0] + A[1] * B[1]
    magnitude_A = math.sqrt(A[0]**2 + A[1]**2)
    magnitude_B = math.sqrt(B[0]**2 + B[1]**2)
    cos_theta = dot_product / (magnitude_A * magnitude_B)
    return math.degrees(math.acos(cos_theta))
