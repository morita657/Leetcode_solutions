from collections import defaultdict
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazineDict = defaultdict(int)
        for i in range(len(magazine)):
            magazineDict[magazine[i]] +=1
        for j in range(len(ransomNote)):
            if magazineDict[ransomNote[j]] and magazineDict[ransomNote[j]]>0:
                magazineDict[ransomNote[j]] -=1
            else:
                return False
        return True

def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    # For each character, c,  in the ransom note.
    for c in ransomNote:
        # If there are none of c left in the String, return False.
        if c not in magazine:
            return False
        # Find the index of the first occurrence of c in the magazine.
        location = magazine.index(c)
        # Use splicing to make a new string with the characters 
        # before "location" (but not including), and the characters 
        #after "location". 
        magazine = magazine[:location] + magazine[location + 1:]
    # If we got this far, we can successfully build the note.
    return True