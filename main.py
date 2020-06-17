def get_primes_v1(limit):
  prime = [i for i in range(limit + 1)]
  for i in prime:
    for j in range(2, prime[i]+1):
      if prime[i] % j == 0:
        prime[i] = False
  prime[1] = False
  return list(filter(None, prime))


def get_primes_v2(limit):
  prime = [i for i in range(limit + 1)]
  for i in prime:
    for j in range(2, int(prime[i] / 2 + 1)):
      if prime[i] % j == 0:
        prime[i] = False
  prime[1] = False
  return list(filter(None, prime))


def get_primes_v3(limit):
  prime = [i for i in range(limit + 1)]
  for i in prime:
    for j in range(2, int(prime[i] ** 0.5 + 1)):
      if prime[i] % j == 0:
        prime[i] = False
  prime[1] = False
  return list(filter(None, prime))


def get_primes_v4(limit):
  prime = [value for value in range(1, limit + 1, 2)]
  for i in range(len(prime)):
    for j in range(3, int(prime[i] ** 0.5 + 1), 2):
      if prime[i] % j == 0:
        prime[i] = False
  prime[0] = 2
  return list(filter(None, prime))


def get_primes_v5(limit):
  prime = [i for i in range(limit + 1)]
  for i in range(2, int(limit ** 0.5) + 1):
    for j in range(i * 2, limit + 1, i):
      prime[j] = False
  prime[1] = False
  return list(filter(None, prime))


if __name__ == "__main__":
  num = 100
  print(get_primes_v1(num))
  print(get_primes_v2(num))
  print(get_primes_v3(num))
  print(get_primes_v4(num))
  print(get_primes_v5(num))
