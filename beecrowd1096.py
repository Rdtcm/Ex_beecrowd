i = 1
j = 7
print(f"I={i} J={j}")
for k in range(5):
    for u in range(2):
        i = i
        j -= 1
        print(f"I={i} J={j}")
    j = 7
    i += 2
    if k < 4:
        print(f"I={i} J={j}")
  
    	

