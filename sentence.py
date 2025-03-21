sentence= input("Enter a sentence: ")
vowel= "aeiouAEIOU"
count=0
for i in sentence:
    if i in vowel:
        count+=1
print("The number of vowels in the sentence is: ", count)