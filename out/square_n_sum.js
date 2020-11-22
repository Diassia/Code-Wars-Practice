"use strict";
// Complete the square sum function so that it squares each number passed into it and then sums the results together.
Object.defineProperty(exports, "__esModule", { value: true });
// For example, for [1, 2, 2] it should return 9 because 1^2 + 2^2 + 2^2 = 9.
function squareSum(numbers) {
    var total = 0;
    numbers.forEach(function (element) {
        var square = element * element;
        total += square;
    });
    return total;
}
exports.squareSum = squareSum;
console.log(squareSum([2, 2]));
// CodeWars solution:
//     export function squareSum(numbers: number[]): number {
//         return numbers.reduce((prev, curr) => prev + curr * curr, 0);
//     }
//# sourceMappingURL=square_n_sum.js.map