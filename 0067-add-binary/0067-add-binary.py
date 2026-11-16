
class Solution:
    def addBinary(self, a: str, b: str) -> str:

        i = len(a) - 1
        j = len(b) - 1

        carry = 0
        result = []

        while i >= 0 or j >= 0 or carry:

            digit1 = int(a[i]) if i >= 0 else 0
            digit2 = int(b[j]) if j >= 0 else 0

            total = digit1 + digit2 + carry

            digit = total % 2
            carry = total // 2

            result.append(str(digit))

            i -= 1
            j -= 1

        return ''.join(result[::-1])
