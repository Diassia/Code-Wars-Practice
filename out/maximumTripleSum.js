"use strict";
// Task
// Given an array/list [] of n integers , find maximum triplet sum in the array Without duplications .
Object.defineProperty(exports, "__esModule", { value: true });
exports.maxTriSum = void 0;
// Notes :
// Array/list size is at least 3 .
// Array/list numbers could be a mixture of positives , negatives and zeros .
// Repetition of numbers in the array/list could occur , So (duplications are not included when summing).
function maxTriSum(nums) {
    var num_set = new Set(nums.sort(function (a, b) { return a - b; }));
    var total_array = (Array.from(num_set)).slice(-3);
    return total_array.reduce(function (a, b) { return a + b; });
}
exports.maxTriSum = maxTriSum;
console.log(maxTriSum([2, 9, 13, 10, 5, 2, 9, 5])); // expect 32
console.log(maxTriSum([2, 1, 8, 0, 6, 4, 8, 6, 2, 4])); // expect 18
//# sourceMappingURL=maximumTripleSum.js.map