type DynamicArray struct {
    data []int
    len int
    cap int
}

func NewDynamicArray(capacity int) *DynamicArray {
    return &DynamicArray{
        data: make([]int, 0, capacity),
        len: 0,
        cap: capacity,
    }
}

func (da *DynamicArray) Get(i int) int {
    return da.data[i]
}

func (da *DynamicArray) Set(i int, n int) {
    da.data[i] = n
}

func (da *DynamicArray) Pushback(n int) {
    da.data = append(da.data, n)
    da.len++
    if da.len > da.cap {
        da.resize()
    }
}

func (da *DynamicArray) Popback() int {
    da.len--
    x := da.data[da.len]
    da.data = da.data[:da.len]
    return x
}

func (da *DynamicArray) resize() {
    da.cap = da.cap * 2
}

func (da *DynamicArray) GetSize() int {
    return da.len
}

func (da *DynamicArray) GetCapacity() int {
    return da.cap
}
