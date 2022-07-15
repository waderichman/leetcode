class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        characters = {                                               
            '2': 'abc',                                                       
            '3': 'def',                                                        
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        if len(digits) == 0: 
            return []                 
        if len(digits) == 1: 
            return list(characters[digits])
        res = []
        for i in characters[digits[0]]:
            for j in self.letterCombinations(digits[1:]):
                res.append(i+j)
        return res