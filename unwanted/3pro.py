s=(input("enter a sentence:"); 
   print(s)
   word=s.split()
   print(word)
for i in word:
   print(f"{i} occurs {word.count(i)}times")
