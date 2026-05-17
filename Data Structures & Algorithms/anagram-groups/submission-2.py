class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorting_dict = {}
        for word in strs:
            normalized_word=''.join(sorted(word))
            if normalized_word not in sorting_dict:
                sorting_dict[normalized_word]=[word]
            else:
                sorting_dict[normalized_word].append(word)
        return list(sorting_dict.values())