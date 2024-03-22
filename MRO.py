locals()def new_mro(ls,new_element):
    final_mro = []
    final_mro.append(new_element)
    for i in range(len(ls)):
        found = False  # Reset found for each sublist
        for j in ls[i]:
            for k in ls[(i + 1):]:
                if j in k:
                    found = True
                    break
            if found:
                break
            else:
                if j not in final_mro:  # Append unique elements
                    final_mro.append(j)
    return final_mro

hierarchy = [['B', 'A', 'O'], ['C', 'A', 'O'], ['A', 'O']]
print(new_mro(hierarchy,'D'))

