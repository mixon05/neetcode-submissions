class DynamicArray { 
    data = []
    capacity = 0
    length = 0
    /**
     * @constructor
     * @param {number} capacity
     */
    constructor(capacity) {
        this.capacity = capacity
        this.data = new Array(capacity).fill(0)
        this.length = 0
    }

    /**
     * @param {number} i
     * @returns {number}
     */
    get(i) {
        return this.data[i]
    }

    /**
     * @param {number} i
     * @param {number} n
     * @returns {void}
     */
    set(i, n) {
        this.data[i] = n
    }

    /**
     * @param {number} n
     * @returns {void}
     */
    pushback(n) {
        if (this.length === this.capacity) {
            this.resize()
        }
        this.data[this.length] = n
        this.length++
    }

    /**
     * @returns {number}
     */
    popback() {
        this.length--
        return this.data[this.length]
    }

    /**
     * @returns {void}
     */
    resize() {
        this.capacity *= 2
        const newData = new Array(this.capacity).fill(0)
        for (let i = 0; i < this.length; i++) {
            newData[i] = this.data[i]
        }
        this.data = newData
    }

    /**
     * @returns {number}
     */
    getSize() {
        return this.length
    }

    /**
     * @returns {number}
     */
    getCapacity() {
        return this.capacity
    }
}
