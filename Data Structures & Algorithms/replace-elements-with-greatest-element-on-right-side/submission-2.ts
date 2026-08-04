class Solution {
    replaceElements(arr: number[]): number[] {
        const out = new Array(arr.length);
        let maxRight = -1;

        for (let i = arr.length - 1; i >= 0; --i) {
            out[i] = maxRight;
            maxRight = Math.max(maxRight, arr[i]);
        }

        return out;
    }
}