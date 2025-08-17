from typing import List
from collections import defaultdict


def groupAnagrams(strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for i in range(len(strs)):
            s = "".join(sorted(strs[i]))
            
            d[s].append(strs[i])

        return [val for val in d.values()]