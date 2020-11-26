"use strict";
// We want an array, but not just any old array, an array with contents!
Object.defineProperty(exports, "__esModule", { value: true });
exports.arr = void 0;
// Write a function that produces an array with the numbers 0 to N-1 in it.
// For example, the following code will result in an array containing the numbers 0 to 4:
// arr(5) // => [0,1,2,3,4]
function range(start, end) {
    var array = [];
    for (var i = start; i <= end; i++) {
        array.push(i);
    }
    return array;
}
var arr = function (n) {
    if (n === void 0) { n = 0; }
    var range_array = range(0, (n - 1));
    return range_array;
};
exports.arr = arr;
console.log(exports.arr(10));
// CodeWars solution:
//     xport const arr = (n = 0): number[] => Array.from({length: n}, (_, i) => i);
//# sourceMappingURL=fillingArray.js.map