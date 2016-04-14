
def gcd(a, b):

    if a % b is 0:
        return b
    else:
        return gcd(a, a % b)

print gcd(12323123112312312, 60)
