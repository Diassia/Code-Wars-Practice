"use strict";
// Return the number (count) of vowels in the given string.
Object.defineProperty(exports, "__esModule", { value: true });
exports.Kata = void 0;
// We will consider a, e, i, o, u as vowels for this Kata (but not y).
// The input string will only consist of lower case letters and/or spaces.
// export class Kata {
//     static getCount(str: string) {
//         let vowelList = 'aeiou';
//         let vcount = 0;
//         for (let x = 0; x < str.length; x++) {
//             if (vowelList.indexOf(str[x]) !== -1) {
//                 vcount += 1;
//             }
//         }
//         return vcount;
//     }
// }
var Kata = /** @class */ (function () {
    function Kata() {
    }
    Kata.getCount = function (str) {
        var m = str.match(/[aeiou]/gi); // g makes it search the whole string, i makes it case-insensitive
        return m === null ? 0 : m.length; // return 0 if there are no vowels
    };
    return Kata;
}());
exports.Kata = Kata;
console.log(Kata.getCount("abracadabra"));
//# sourceMappingURL=vowelCount.js.map