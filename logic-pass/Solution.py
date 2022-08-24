
# ┏━━━━━━━━━━━━━━━━ NOTE Author ━━━━━━━━━━━━━━━━┓
# ┃       Name: Hussein Abbas Abduljaleel       ┃
# ┃      Github/Telegram/IG: hussain7abbas      ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛


# Q1 - (Method) remove any given character from a String
class Solution():
    def Q1_removeChar(string: str, char: chr):
        return string.replace(char, '')


# Q2 - (Program) find all prime numbers up to a given range of numbers
def Q2_findPrimes(stopNum: int) -> list:
    primes = [1]
    for num in range(1, stopNum):
        for j in range(2, num):
            if (num % j) == 0:
                break
            if (j == num-1):
                primes.append(num)
    return primes


# Q3 - (Function) count how many the given character repeated in a given string
def Q3_countChar(string: str, char: chr) -> int:
    return string.count(char)
