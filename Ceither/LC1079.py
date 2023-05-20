from itertools import permutations
def numTilePossibilities(self, tiles: str) -> int:
    ans = []
    for i in range(1, len(tiles) + 1):
        ans += list(set(permutations(tiles, i)))
    return len(ans)