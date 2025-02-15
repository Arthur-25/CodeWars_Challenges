'''
Given a list and a number, create a new list that contains each number of list at most N times, without reordering.
For example if the input number is 2, and the input list is [1,2,3,1,2,1,2,3], you take [1,2,3,1,2],
drop the next [1,2] since this would lead to 1 and 2 being in the result 3 times, and then take 3, which leads to [1,2,3,1,2,3].
With list [20,37,20,21] and number 1, the result would be [20,37,21].

'''

def impede_repetir(data,num,numero):
    repetidos = 0
    for number in range(len(data) - 1, 0, -1):
        if (data.count(numero) > num and data[number] == numero):
            data[number] = None
            repetidos += 1
    return data
def delete_nth(order,max_e):
    listaa = []
    for number in range(0, len(order), 1):
        if order[number] not in listaa:
            listaa.append(order[number])
            order = impede_repetir(order, max_e, order[number])

    for number in range(0, len(order), 1):

        if None in order:
            order.remove(None)
    return order

lista = [1,2,3,1,2,1,2,3]


print(delete_nth(lista,2))
print(delete_nth([20, 37, 20, 21], 1))
print(delete_nth([1, 1, 3, 3, 7, 2, 2, 2, 2], 3))