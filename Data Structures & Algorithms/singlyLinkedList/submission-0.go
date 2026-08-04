type LinkedList struct {
    data int
    next *LinkedList
}

func NewLinkedList() *LinkedList {
    return &LinkedList{
        data: 0,
        next: nil,
    }
}

func (ll *LinkedList) Get(index int) int {
    currll := ll.next 
    for i := 0; i < index; i++ {
        if currll == nil {
            return -1
        }
        currll = currll.next
    }
    if currll == nil {
        return -1
    }
    return currll.data
}

func (ll *LinkedList) InsertHead(val int) {
    newNode := &LinkedList{
        data: val,
        next: ll.next,
    }
    ll.next = newNode
}

func (ll *LinkedList) InsertTail(val int) {
    currll := ll
    for currll.next != nil {
        currll = currll.next
    }
    currll.next = &LinkedList{
        data: val,
        next: nil,
    }
}

func (ll *LinkedList) Remove(index int) bool {
    currll := ll
    for i := 0; i < index; i++ {
        if currll.next == nil {
            return false
        }
        currll = currll.next
    }
    
    if currll.next == nil {
        return false
    }
    currll.next = currll.next.next
    return true
}

func (ll *LinkedList) GetValues() []int {
    currll := ll.next
    var arr []int 
    for currll != nil {
        arr = append(arr, currll.data)
        currll = currll.next
    }
    return arr
}

func (ll *LinkedList) find(index int) *LinkedList {
    currll := ll.next
    for i := 0; i < index; i++ {
        if currll == nil {
            return nil
        }
        currll = currll.next
    }
    return currll
}