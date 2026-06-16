#this is a vibe-coded visvalization of number vs number of primes upto that point
#please download matplotlib before hand
import matplotlib.pyplot as plt
from math import sqrt

def sieve(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(sqrt(n)) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    return is_prime

def prime_count_curve(n):
    is_prime = sieve(n)

    x = []
    y = []
    count = 0

    for i in range(n + 1):
        if is_prime[i]:
            count += 1
        x.append(i)
        y.append(count)

    return x, y

def main():
    N = int(input("Enter upper limit: "))

    x, y = prime_count_curve(N)

    plt.figure(figsize=(10, 5))
    plt.plot(x, y, linewidth=2)

    plt.title("Number vs Count of Primes (π(n))")
    plt.xlabel("n")
    plt.ylabel("Number of primes ≤ n")
    plt.grid(True)

    plt.show()

if __name__ == "__main__":
    main()
