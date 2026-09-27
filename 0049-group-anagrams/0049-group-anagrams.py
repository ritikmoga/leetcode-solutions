from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # Map sorted strings to their original anagrams
        anagram_map = defaultdict(list)
        
        for s in strs:
            # Sort the characters of the string to form the key
            # e.g., ''.join(sorted("tea")) -> "aet"
            sorted_key = "".join(sorted(s))
            anagram_map[sorted_key].append(s)
            
        # Return the collected groups of anagrams
        return list(anagram_map.values())
