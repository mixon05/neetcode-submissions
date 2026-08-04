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
    node := ll.find(index)
    if node == nil {
        return -1
    }
    return node.data
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
    var prev *LinkedList
    if index == 0 {
        prev = ll
    } else {
        prev = ll.find(index - 1)
    }

    if prev == nil || prev.next == nil {
        return false
    }

    prev.next = prev.next.next
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
    if index < 0 {
        return nil
    }
    currll := ll.next
    for i := 0; i < index && currll != nil; i++ {
        currll = currll.next
    }
    return currll
}