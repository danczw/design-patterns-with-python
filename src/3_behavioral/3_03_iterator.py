# iterator method - behavioral design pattern
#   allows to traverse elements of collections without taking the exposure of
#   in-depth details of the elements

# create iterator methods
# - Single Responsibility Principle: easy to extract huge algorithms into
#   separate classes
# - Open/Closed Principle: passing new iterators and collections into code does
#   not break code and can easily be installed into it
# - Easy to use Interface: makes interface really simple to use and also
#   supports the variations in the traversal of collections
def alphabets_upto(letter):
    # counts by word numbers, up to a maximum of five
    for i in range(65, ord(letter)+1):
        yield chr(i)


# run method
if __name__ == '__main__':
    alphabets_upto_K = alphabets_upto('K')
    alphabets_upto_M = alphabets_upto('M')

    for alpha in alphabets_upto_K:
        print(alpha, end=" ")

    print()

    for alpha in alphabets_upto_M:
        print(alpha, end=" ")
    print()