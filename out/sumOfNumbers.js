"use strict";
// Given two integers a and b, which can be positive or negative, find the sum of all the integers between including them too and return it. 
//If the two numbers are equal return a or b.
// Note: a and b are not ordered!
Object.defineProperty(exports, "__esModule", { value: true });
exports.getSum = void 0;
function getSum(a, b) {
    var array = [];
    // let array_negative = []
    if (a > b) {
        for (var i = a; i >= b; i--) {
            array.push(i);
        }
    }
    else {
        for (var i = a; i <= b; i++) { // start, stop, increment
            // if (i < 0) {
            //     array_negative.push(i)
            // }else{
            array.push(i);
            // }
        }
    }
    // let array_sum1 = 
    // let array_sum2 = array_negative.reduce((a, b) => a + b, 0)
    // 
    return array.reduce(function (a, b) { return a + b; }, 0);
}
exports.getSum = getSum;
console.log(getSum(0, -1)); // expect -1
console.log(getSum(0, 1)); // expect 1
console.log(getSum(3, 40));
//# sourceMappingURL=sumOfNumbers.js.map