#[*EXPRESSION* for *ITEM* in *LIST* if *CONDITION*]
listy = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
odd_even = ["even" if item%2 == 0 else "odd" for item in listy]
print(odd_even)

#filtered = [2*num for num in numbersequence if num%2 == 0]
triple = [num for num in range(1,11) if num%3 == 0]
print(triple)
