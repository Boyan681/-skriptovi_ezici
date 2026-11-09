n = int(input())
while n < 5:
    n = int(input())

broi_dvoiki = 0
posledna_dvoika = None

for p in range(2, n - 1):
    q = p + 2 
    
    is_p_prime = True
    d = 2
    while d * d <= p:
        if p % d == 0:
            is_p_prime = False
            break
        d += 1
    is_q_prime = True
    d = 2
    while d * d <= q:
        if q % d == 0:
            is_q_prime = False
            break
        d += 1
        
    if is_p_prime and is_q_prime:
        print(f"({p}, {q})")
        broi_dvoiki += 1
        posledna_dvoika = (p, q)

print("Number of twins:", broi_dvoiki)
if posledna_dvoika:
    print("Biggest twins:", posledna_dvoika)