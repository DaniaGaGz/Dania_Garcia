#[*EXPRESSION* for *ITEM* in *LIST* if *CONDITION*]
odd_even = ["even" if item%2 == 0 else "odd" for item in range(1,21)]
print(odd_even)

#filtered = [2*num for num in numbersequence if num%2 == 0]
triple = [num for num in range(1,11) if num%3 == 0]
print(triple)