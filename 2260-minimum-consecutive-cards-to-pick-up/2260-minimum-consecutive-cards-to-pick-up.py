class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        cardmap = {}
        ans = 10**5 + 1
        minimum = -1
        for idx, card in enumerate(cards):
            if card in cardmap:
                cardmap[card].append(idx)
            else:
                cardmap[card] = [idx]
        print(cardmap)
        for card in cardmap:
            l = 0
            r = l+1
            
            while r < len(cardmap[card]):
                ans = min(ans,cardmap[card][r] - cardmap[card][l] + 1)
                r += 1
                l += 1
        return minimum if ans == 10**5 + 1 else ans
                
            