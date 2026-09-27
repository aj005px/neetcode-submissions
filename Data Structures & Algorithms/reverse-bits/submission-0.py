class Solution:
    def reverseBits(self, n: int) -> int:
        n_string = bin(n)[2:].zfill(32)
        return int(n_string[::-1], 2)

