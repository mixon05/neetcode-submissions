class KthLargest {
    k: number;
    nums: number[];
    /**
     * @param {number} k
     * @param {number[]} nums
     */
    constructor(k: number, nums: number[]) {
        this.k = k;
        this.nums = nums;
    }

    /**
     * @param {number} val
     * @return {number}
     */
    add(val: number): number {
        this.nums.push(val);
        this.nums = this.nums.sort((x, y) => y - x);
        return this.nums[this.k - 1];
    }
}