class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # create count_dict of letters in word1 and word2
        word1=s
        word2=t
        count_dict_word1 = {}
        count_dict_word2 = {}
        if len(word1)!=len(word2) or len(word1)==0 or len(word2)==0:
            return False
        longer_word = max(len(word1), len(word2))
        for x in range (0, longer_word):
            if x <= len(word2):
                if word2[x] not in count_dict_word2:
                    count_dict_word2[word2[x]]=1
                else:
                    count_dict_word2[word2[x]]+=1
            if x <= len(word1):
                if word1[x] not in count_dict_word1:
                    count_dict_word1[word1[x]]=1
                else:
                    count_dict_word1[word1[x]]+=1
        return count_dict_word1==count_dict_word2