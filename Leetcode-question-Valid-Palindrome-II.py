def validPalindrome(self, s: str) -> bool:
        i=0 #pointer from left
        j=len(s)-1 #pointer from right
		#loop will work till both the pointers don't coincide or cross each other
        while i<j:
            if s[i]!=s[j]: #if any two characters are not equal then check substring between i and j pointers
			#means firstly remove the 1 character from right s[i] only i.e, s[i+1:j+1] substring need to be checked if palindrome
			#or you can remove the s[j] left character i.e, substring is s[i:j] which need to be checked if palindrome
			#means we have checked by removing any one character, if still string is palindrome, return true, otherwise false
			
                if s[i+1:j+1]==s[i+1:j+1][::-1] or s[i:j]==s[i:j][::-1]:
                    return True
                else:
                    return False
            i+=1
            j-=1
			
        return True  #thats the condition when whole string is already palindrome 
		#if string is "abba" (then romoving any b can keep the string still palindrome)
		#or if string is "aba" (then removing b can keep the string still palindrome)
