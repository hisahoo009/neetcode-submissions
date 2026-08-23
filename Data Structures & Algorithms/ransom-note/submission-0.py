class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        if len(magazine) < len(ransomNote):
            return False
                    
        freq_ransom = {char: ransomNote.count(char) for char in set(ransomNote)}
        freq_magazine = {char: magazine.count(char) for char in set(magazine)}

        for letter, freq in freq_ransom.items():
            # letter exist in magazine 
            if letter in freq_magazine.keys():
                count_mag = freq_magazine[letter]
                if count_mag < freq:
                    return False

            # letter does not exist in magazine 
            if letter not in freq_magazine.keys():
                return False
        
        return True