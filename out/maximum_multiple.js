"use strict";
// Task
// Given a Divisor and a Bound , Find the largest integer N , Such That ,
Object.defineProperty(exports, "__esModule", { value: true });
exports.maxMultiple = void 0;
// Conditions :
// N is divisible by divisor
// N is less than or equal to bound
// N is greater than 0.
// Notes
// The parameters (divisor, bound) passed to the function are only positive values .
// It's guaranteed that a divisor is Found .
function maxMultiple(divisor, bound) {
    var array = [];
    var array2 = [];
    for (var count = 0; count <= bound; count++) { // iterates through numbers up to bound and pushes result to "array"
        array.push(count);
    }
    for (var _i = 0, array_1 = array; _i < array_1.length; _i++) { // iterates through "array" and checks if element is divisible by divisor, pushes result to "array2"
        var i = array_1[_i];
        if (i % divisor == 0) {
            array2.push(i);
        }
    }
    ;
    return array2[array2.length - 1]; // returns last element in array2
}
exports.maxMultiple = maxMultiple;
console.log(maxMultiple(2, 7));
console.log(maxMultiple(3, 10));
console.log(maxMultiple(10, 50));
//# sourceMappingURL=maximum_multiple.js.map