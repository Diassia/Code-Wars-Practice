"use strict";
// Scenario
// Now that the competition gets tough it will Sort out the men from the boys .
Object.defineProperty(exports, "__esModule", { value: true });
exports.menFromBoys = void 0;
// Men are the Even numbers and Boys are the odd!alt!alt
// Task
// Given an array/list [] of n integers , Separate The even numbers from the odds , or Separate the men from the boys!alt!alt
// Notes
// Return an array/list where Even numbers come first then odds
// Since , Men are stronger than Boys , Then Even numbers in ascending order While odds in descending .
// Array/list size is at least *4*** .
// Array/list numbers could be a mixture of positives , negatives .
// Have no fear , It is guaranteed that no Zeroes will exists .!alt
// Repetition of numbers in the array/list could occur , So (duplications are not included when separating).
// Men: Even, ascending
// Boys: Odd, decending
function menFromBoys(arr) {
    var menArray = [];
    var boyArray = [];
    for (var i = 0; i < arr.length; i++) {
        if (arr[i] % 2 == 0) {
            if (menArray.includes(arr[i])) {
                continue;
            }
            else {
                menArray.push(arr[i]);
            }
        }
        else {
            if (boyArray.includes(arr[i])) {
                continue;
            }
            else {
                boyArray.push(arr[i]);
            }
        }
    }
    menArray.sort(function (a, b) { return a - b; });
    boyArray.sort(function (a, b) { return b - a; });
    return menArray.concat(boyArray);
}
exports.menFromBoys = menFromBoys;
console.log(menFromBoys([7, 3, 14, 17])); // expect [14, 17, 7, 3]
console.log(menFromBoys([2, 43, 95, 90, 37])); //expect [2, 90, 95, 43, 37]
//# sourceMappingURL=sortMenFromBoys.js.map