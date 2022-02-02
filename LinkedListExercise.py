class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None;

    def print(self):
        if self.head is None:
            print("Linked List is empty");
            return;
        itr = self.head;
        lstr ='';
        while itr:
            lstr = lstr + str(itr.data)+'-->'
            itr = itr.next;
        print(lstr);

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_values(self,datalist):
        self.head = None
        for data in datalist:
            self.insert_at_end(data)

    def insert_after_value(self, data_after, data_to_insert):
        itr = self.head
        while itr.data != data_after:
            itr = itr.next
        node = Node(data_to_insert, itr.next);
        itr.next =  node

        #Search for first occurance of data_after value in linked list
        #Now insert data_to_insert after data_after node

    #
    def remove_by_value(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return
        itr = self.head;
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next

        # Remove first node that contains data


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_end('aa')
    ll.insert_values(["banana", "mango", "grapes", "orange"])
    ll.print()
    ll.insert_after_value("mango", "apple")  # insert apple after mango
    ll.print()
    ll.remove_by_value("orange")  # remove orange from linked list
    ll.print()
    ll.remove_by_value("figs")
    ll.print()
    ll.remove_by_value("banana")
    ll.remove_by_value("mango")
    ll.remove_by_value("apple")
    ll.remove_by_value("grapes")
    ll.print()
