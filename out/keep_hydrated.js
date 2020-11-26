"use strict";
// Nathan loves cycling.
Object.defineProperty(exports, "__esModule", { value: true });
exports.litres = void 0;
// Because Nathan knows it is important to stay hydrated, he drinks 0.5 litres of water per hour of cycling.
// You get given the time in hours and you need to return the number of litres Nathan will drink, rounded to the smallest value.
// For example:
// time = 3 ----> litres = 1
// time = 6.7---> litres = 3
// time = 11.8--> litres = 5
function litres(time) {
    return Math.floor(time * 0.5);
}
exports.litres = litres;
var time = 10;
console.log(litres(time));
//# sourceMappingURL=keep_hydrated.js.map