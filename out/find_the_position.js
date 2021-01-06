"use strict";
// When provided with a letter, return its position in the alphabet.
Object.defineProperty(exports, "__esModule", { value: true });
exports.position = void 0;
// Input :: "a"
// Ouput :: "Position of alphabet: 1"
function position(alphabet) {
    var alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'];
    // let alphabet_number = alphabet_list.indexOf(alphabet);
    // let position_number = alphabet_number + 1;
    // return "Position of alphabet: " + position_number;
    return "Position of alphabet: " + (alphabet_list.indexOf(alphabet) + 1);
}
exports.position = position;
console.log(position("a"));
// alphabet_list.indexOf(position_number);
//# sourceMappingURL=find_the_position.js.map