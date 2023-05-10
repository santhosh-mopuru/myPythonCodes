class Node:
    def __init__(self, dataval=None) -> None:
        self.dataval=dataval
        self.nextval=None
        
class SLinkedList:
    def __init__(self) -> None:
        self.headval=None
    
    def printList(self):
        
        printval=self.headval
        #print(printval.dataval)
        
        while printval is not None:
            print("--->",printval.dataval,end="")
            printval=printval.nextval
    
    def InsertAtBegin(self,newdata):
        Newnode=Node(newdata)
        
        Newnode.nextval=self.headval
        self.headval=Newnode
        print("\n After inserting new node at the beginning")
        self.printList()

    def InsertInBetween(self,thatNode,thisNode,newdata):
        Newnode = Node(newdata)
        print(Newnode.dataval)
        input("Press Enter")
        tempnode=Node("")
        printval=self.headval
        nodeorder=0
        while printval is not None:
            nodeorder+=1
            if(printval.dataval==thatNode):
                nodenum1=nodeorder
                print("Found 1st node")
            elif(printval.dataval==thisNode):
                nodenum2=nodeorder
                print("Found 2nd node")
            printval=printval.nextval

        if(nodenum2-nodenum1==1):
            
            printval1=self.headval
            while printval1 is not None:
                nodevalue=printval1.dataval
                
                if(nodevalue==thatNode):
                    
                    Newnode.nextval=printval1.nextval
                    
                    printval1.nextval=Newnode
                    
                    break
                else:
                    printval1=printval1.nextval
                    
        else:
            print("There are more Nodes between this and that node")
        
        self.printList()
    
    def RemoveNode(self,removekey):
        Headval=self.headval
        print(self.headval.dataval)
        print(removekey)
        if(self.headval.dataval==removekey):
            self.headval=Headval.nextval
            Headval=None
            self.printList()
            return
        else:
            print("Yet to work on this")
            Headval=Headval.nextval
            while Headval is not None:
                if(Headval.dataval==removekey):
                    break
                prenoderef=Headval
                Headval=Headval.nextval

            prenoderef.nextval=Headval.nextval    
            Headval=None
            self.printList()
            return

def main():
    list1=SLinkedList()
    list1.headval=Node("Mon")
    e2=Node("Tue")
    e3=Node("Wed")
    list1.headval.nextval=e2
    e2.nextval=e3
    e4=Node("Thurs")
    e3.nextval=e4

    list1.printList()
    list1.InsertAtBegin("Sun")
    list1.InsertInBetween("Mon","Tue","Holi")
    list1.RemoveNode("Thurs")


if __name__ == "__main__":
    main()




