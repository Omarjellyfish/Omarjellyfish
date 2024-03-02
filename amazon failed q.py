def mergesortorder(order, lista):
    mid = len(lista) // 2
    if len(lista) > 1:


        left = lista[:mid]
        right = lista[mid:]

        mergesortorder(order, left)
        mergesortorder(order, right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            x = 0


            while True:
                ll = len(left[i])
                lr = len(right[j])
                m = min(lr, ll)  # max length possible for x >> len of smaller array
                print('x:',x,'  i:',i,'  j:',j,'  left:',left,'  right',right,'    m:',m)


                if left[i][x] == right[j][x]:
                    x += 1
                    if x == m:
                        if ll < lr:

                            lista[k] = left[i]
                            i += 1
                            k += 1
                            break
                        else:
                            lista[k] = right[j]
                            j += 1
                            k += 1
                            break


                else:

                    if order[left[i][x]] > order[right[j][x]]:

                        lista[k] = right[j]
                        j += 1

                    else:

                        lista[k] = left[i]
                        i += 1

                    k += 1
                    break

            while j < len(right):
                lista[k] = right[j]
                j += 1
                k += 1
            while i < len(left):
                lista[k] = left[i]
                i += 1
                k += 1


    return lista


s = 'hcdabef'
hashmap = {}
y = 0
for char in s:
    hashmap[char] = y
    y += 1
codes = ['abc', 'edh', 'hce', 'hcde', 'hcef','hcdefb']
print(hashmap)
g=mergesortorder(hashmap, codes)

print(codes)
