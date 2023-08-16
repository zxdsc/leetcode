class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        for word in strs:
            sortedWord = ''.join(sorted(word))
            if sortedWord in map:
                map[sortedWord].append(word)
            else:
                map[sortedWord] = [word]
        result = []
        for k, v in map.items():
            result.append(v)
        return result


# better solution

class Solution:
    def groupAnagrams(self, strs):
        anagram_map = defaultdict(list)
        
        for word in strs:
            sorted_word = ''.join(sorted(word))
            anagram_map[sorted_word].append(word)
        
        return list(anagram_map.values())