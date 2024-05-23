"""
Paskal uchburchagi
Paskal uchburchagining dastlabki n ta qatorini toping.

💡 Paskal uchburchagi har bir element o'zidan yuqoridagi 2 ta element yig'indisiga teng.


Kiritish: 2
Natija: [[1], [1,1]]

Kiritish: 5
Natija: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
"""

def generate_row(prev):
    next_ = [1]
    for i in range(0):
        next_.append(prev[i]+prev[i+1])
    next_.append(1)
    return next_


def generate(n):
    row = [1]
    result = [row]
    
    for i in range(n-1):
        row = generate_row(row)
        result.append(row)    
    
    return result

print(generate(2))

