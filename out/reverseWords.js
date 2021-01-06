"use strict";
// Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.
Object.defineProperty(exports, "__esModule", { value: true });
exports.reverseWords = void 0;
// Examples
// "This is an example!" ==> "sihT si na !elpmaxe"
// "double  spaces"      ==> "elbuod  secaps"
function reverseWords(str) {
    var sentenceString = str;
    var stringArray = sentenceString.split(/(\s+)/);
    var arrayLength = stringArray.length;
    var newString = '';
    for (var i = 0; i < arrayLength; i++) {
        var wordString = stringArray[i];
        var wordArray = wordString.split('');
        newString += wordArray.reverse().join('');
    }
    return newString;
}
exports.reverseWords = reverseWords;
console.log(reverseWords('The quick brown fox jumps over the lazy dog.'));
console.log(reverseWords('apple'));
console.log(reverseWords('a b c d'));
console.log(reverseWords('double  spaced  words'));
//# sourceMappingURL=reverseWords.js.map