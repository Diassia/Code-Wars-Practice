// Task
// Given an array/list [] of n integers , find maximum triplet sum in the array Without duplications .

// Notes :
// Array/list size is at least 3 .

// Array/list numbers could be a mixture of positives , negatives and zeros .

// Repetition of numbers in the array/list could occur , So (duplications are not included when summing).

export function maxTriSum(nums: number[]): number {
    let num_set: Set<number> = new Set(nums.sort((a, b) => a - b));
    let total_array: number[] = (Array.from(num_set)).slice(-3);
    return total_array.reduce((a, b) => a + b);
}

console.log(maxTriSum([2, 9, 13, 10, 5, 2, 9, 5])); // expect 32
console.log(maxTriSum([2, 1, 8, 0, 6, 4, 8, 6, 2, 4])); // expect 18