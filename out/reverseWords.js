"use strict";
// Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.
Object.defineProperty(exports, "__esModule", { value: true });
exports.reverseWords = void 0;
// Examples
// "This is an example!" ==> "sihT si na !elpmaxe"
// "double  spaces"      ==> "elbuod  secaps"
function reverseWords(str) {
    var sentence_string = str;
    var string_array = sentence_string.split('');
    return string_array.reverse().join('');
    // let arrayOfString = Array.from(String(sentence_string), String)
    // return "Go for it";
}
exports.reverseWords = reverseWords;
console.log(reverseWords('The quick brown fox jumps over the lazy dog.'));
console.log(reverseWords('apple'));
console.log(reverseWords('a b c d'));
console.log(reverseWords('double  spaced  words'));
//# sourceMappingURL=reverseWords.js.map