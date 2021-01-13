// Ask a small girl - "How old are you?". She always says strange things... Lets help her!

// For correct answer program should return int from 0 to 9.

// Assume test input string always valid and may look like "1 year old" or "5 years old", etc.. The first char is number only.


export {get_age};

function get_age(age: string): number {
    return parseInt(age[0]);
}

console.log(get_age("2 years old"));
console.log(get_age("4 years old"));
console.log(get_age("7 years old"));



// Top CodeWars Solution:
// export { get_age };

// function get_age(age: string): number {
//   return parseInt(age);
// }