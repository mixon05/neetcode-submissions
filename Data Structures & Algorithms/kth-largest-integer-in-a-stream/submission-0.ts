class KthLargest {
    private k: number;
    values = new Map<number, number>();

    constructor(k: number, nums: number[]) {
        this.k = k;
        for (const num of nums) {
            this.values.set(num, (this.values.get(num) || 0) + 1);
        }
    }

    add(val: number): number {
        this.values.set(val, (this.values.get(val) || 0) + 1);

        const sortedKeys = Array.from(this.values.keys()).sort((a, b) => b - a);

        let count = 0;
        for (const key of sortedKeys) {
            count += this.values.get(key)!;
            if (count >= this.k) {
                return key;
            }
        }

        return -1; 
    }
}