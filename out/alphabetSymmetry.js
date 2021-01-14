"use strict";
// Consider the word "abode". We can see that the letter a is in position 1 and b is in position 2. In the alphabet, a and b are also in positions 1 and 2. Notice also that d and e in abode occupy the positions they would occupy in the alphabet, which are positions 4 and 5.
Object.defineProperty(exports, "__esModule", { value: true });
exports.solve = void 0;
// Given an array of words, return an array of the number of letters that occupy their positions in the alphabet for each word. For example,
// solve(["abode","ABc","xyzD"]) = [4, 3, 1]
// See test cases for more examples.
// Input will consist of alphabet characters, both uppercase and lowercase. No spaces.
// let alphabet = {
//     1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j', 11: 'k', 12: 'l', 13: 'm', 14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't', 21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z'
// }
function solve(arr) {
    var final_array = [];
    var letter_calculation = 0;
    arr.forEach(function (word) {
        for (var i = 0; i < word.length; i++) {
            if (word.toUpperCase().charCodeAt(i) == (i + 65)) {
                letter_calculation += 1;
            }
        }
        final_array.push(letter_calculation);
        letter_calculation = 0;
    });
    return final_array;
}
exports.solve = solve;
console.log(solve(["abode", "ABc", "xyzD"])); // expect [4, 3, 1]
console.log(solve(["IAMDEFANDJKL", "thedefgh", "xyzDEFghijabc"])); //expect [6, 5, 7]
//# sourceMappingURL=alphabetSymmetry.js.map