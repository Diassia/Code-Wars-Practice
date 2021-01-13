"use strict";
// Ask a small girl - "How old are you?". She always says strange things... Lets help her!
Object.defineProperty(exports, "__esModule", { value: true });
exports.get_age = void 0;
function get_age(age) {
    return parseInt(age[0]);
}
exports.get_age = get_age;
console.log(get_age("2 years old"));
console.log(get_age("4 years old"));
console.log(get_age("7 years old"));
// Top CodeWars Solution:
// export { get_age };
// function get_age(age: string): number {
//   return parseInt(age);
// }
//# sourceMappingURL=parse_nice_int.js.map