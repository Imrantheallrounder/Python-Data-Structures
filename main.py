from SinglyLinkedList import LinkedList

ll1 = LinkedList()
# ll1.insert_at_begining(1)
# ll1.insert_at_begining(2)
# ll1.insert_at_begining(3)
# ll1.insert_at_end(0)
# ll1.insert_at_end(10)
# ll1.remove_at(4)
# ll1.insert_at(3,"abc")
ll1.insert_values(["apple","banana","guava"])
# ll1.insert_after_value("banana", "orange")
print(ll1.print())
# ll1.insert_after_value("guava", "orange")
# ll1.remove_by_value("as")
ll1.reverse()


print(ll1.print())
print("Length of LL: ", ll1.size())