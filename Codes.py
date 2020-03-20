# print domino tiles
for left in range(7):
    for right in range(left,7):
        print (str(left)+"-"+str(right), end='|')
    print()

#enumerate and list comprenhension usage
z=[(index,x) for index,x in enumerate(list(range(1,11))) if index%2==0 ]

def skip_elements(elements):
	return [x for index,x in enumerate(elements) if index%2==0]  

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']


    
