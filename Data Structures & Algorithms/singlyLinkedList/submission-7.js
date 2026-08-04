class Node {
    constructor(val) {
        this.value = val;
        this.next = null;
    }
}

class LinkedList {
    constructor() {
        this.head = null;
        this.tail = null;
    }

    /**
     * @param {number} index
     * @return {number}
     */
    get(index) {
        let i = 0;
        let node = this.head;
        while (node && i < index) {
            node = node.next;
            i++;
        }
        return node ? node.value : -1;
    }

    /**
     * @param {number} val
     * @return {void}
     */
    insertHead(val) {
        const newNode = new Node(val);
        newNode.next = this.head;
        this.head = newNode;
        if (!this.tail) this.tail = newNode;
    }

    /**
     * @param {number} val
     * @return {void}
     */
    insertTail(val) {
        const newNode = new Node(val);
        if (!this.head) {
            this.head = newNode;
            this.tail = newNode;
            return;
        }
        this.tail.next = newNode;
        this.tail = newNode;
    }

    /**
     * @param {number} index
     * @return {boolean}
     */
    remove(index) {
        if (!this.head) return false;
        if (index === 0) {
            this.head = this.head.next;
            if (!this.head) this.tail = null;
            return true;
        }

        let i = 0;
        let node = this.head;
        while (node && i < index - 1) {
            node = node.next;
            i++;
        }

        if (!node || !node.next) return false;
        if (node.next === this.tail) this.tail = node;
        node.next = node.next.next;
        return true;
    }

    /**
     * @return {number[]}
     */
    getValues() {
        let values = [];
        let node = this.head;
        while (node) {
            values.push(node.value);
            node = node.next;
        }
        return values;
    }
}