# prime.py

def generate_n_primes(N):
    primes  = []
    chkthis = 2
    while len(primes) < N:
        ptest = [chkthis for i in primes if chkthis%i == 0]
        primes  += [] if ptest else [chkthis]
        chkthis += 1
    return primes

print(generate_n_primes(100))
