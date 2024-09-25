import re
def isPalindrome(A):
    if A == "":
        return 1
    A = re.sub('[^a-zA-Z0-9]', '', A)

    if A == "":
        return 1

    A = A.lower()

    i = 0
    j = len(A) - 1
    while i < j:
        if A[i] != A[j]:
            return 0
        i += 1
        j -= 1
    return 1
    
input1 = "A man, a plan, a canal: Panama"

if isPalindrome(input1)== 1:
    print('yes')
else :
    print("no")
    
#     git remote add origin https://github.com/Anurag-git04/meditab.git
# git branch -M main
# git push -u origin main