"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.equalize = void 0;
function equalize(array) {
    var toEqualizeArray = [];
    array.forEach(function (value) {
        var numberCompare = array[0];
        var difference = value - numberCompare;
        if (difference < 0) {
            toEqualizeArray.push(String(difference));
        }
        else {
            toEqualizeArray.push("+" + difference);
        }
        ;
    });
    return toEqualizeArray;
}
exports.equalize = equalize;
console.log(equalize([10, 20, 25, 0]));
console.log(equalize([20, 30, 35, 10]));
console.log(equalize([]));
console.log(equalize([10, 12, 24, 50, 0, 15, 20]));
//Top CodeWar Solution:
// export function equalize(array:number[]):string[]
// {
//   let result = array.map((element) =>
//   {
//     let delta = element - array[0];
//     return ((delta >= 0) ? "+" : "") + delta;
//   });
//   return result;
// }
//# sourceMappingURL=equalizeArray.js.map