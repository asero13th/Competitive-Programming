class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        hashmap = {'W':0}
        minimum = 10**4
        if not blocks:
            return 0
        for i in range(k):
            if blocks[i] == 'W':
                hashmap['W'] += 1
        minimum = min(minimum, hashmap['W'])
        
        i,j = 1,k
        while j < len(blocks):
            if blocks[i - 1] == 'W':
                hashmap['W'] -= 1
            if blocks[j] == 'W':
                hashmap['W'] += 1
            i += 1
            j += 1
            minimum = min(minimum,hashmap['W'])
        return minimum
                
            