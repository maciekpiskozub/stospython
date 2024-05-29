from stos import Stos

stos = Stos()

stos.push(10)
stos.push(20)
stos.push(30)
stos.push(40)

print("Top: ", stos.top)
print("Pop: ", stos.pop)
print("Czy stos jet pusty: ", stos.is_empty())
print(stos.zawartosc)