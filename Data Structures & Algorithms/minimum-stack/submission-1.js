class MinStack {
    constructor() {
        this.data = new Array()
    }

    /**
     * @param {number} val
     * @return {void}
     */
    push(val) {
        this.data.push(val)
    }

    /**
     * @return {void}
     */
    pop() {
        this.data.pop()
    }

    /**
     * @return {number}
     */
    top() {
        return this.data[this.data.length - 1]
    }

    /**
     * @return {number}
     */
    getMin() {
        return Math.min(...this.data)
    }
}
