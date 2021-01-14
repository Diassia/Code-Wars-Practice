// Task
// Given an array/list [] of n integers , find maximum triplet sum in the array Without duplications .

// Notes :
// Array/list size is at least 3 .

// Array/list numbers could be a mixture of positives , negatives and zeros .

// Repetition of numbers in the array/list could occur , So (duplications are not included when summing).

export function maxTriSum(nums: number[]): number {
    let num_set = new Set(nums);
}

console.log(maxTriSum([2, 9, 13, 10, 5, 2, 9, 5]));
console.log(maxTriSum([2, 1, 8, 0, 6, 4, 8, 6, 2, 4]));