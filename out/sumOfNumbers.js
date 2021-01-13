"use strict";
// Given two integers a and b, which can be positive or negative, find the sum of all the integers between including them too and return it. 
//If the two numbers are equal return a or b.
// Note: a and b are not ordered!
Object.defineProperty(exports, "__esModule", { value: true });
exports.getSum = void 0;
function getSum(a, b) {
    var array = [];
    if (a > b) {
        for (var i = a; i >= b; i--) {
            array.push(i);
        }
    }
    else {
        for (var i = a; i <= b; i++) {
            array.push(i);
        }
    }
    return array.reduce(function (a, b) { return a + b; }, 0);
}
exports.getSum = getSum;
console.log(getSum(0, -1)); // expect -1
console.log(getSum(0, 1)); // expect 1
console.log(getSum(3, 40));
// Top CodeWars Solution:
// export function getSum(a: number, b: number): number {
//     const start = a < b ? a : b;
//     const end = start === a ? b : a;
//     let sum = 0;
//     for (let i = start; i <= end; i++) {
//       sum += i;
//     }
//     return sum;
//   }
//# sourceMappingURL=sumOfNumbers.js.map