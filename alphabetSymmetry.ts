// Consider the word "abode". We can see that the letter a is in position 1 and b is in position 2. In the alphabet, a and b are also in positions 1 and 2. Notice also that d and e in abode occupy the positions they would occupy in the alphabet, which are positions 4 and 5.

// Given an array of words, return an array of the number of letters that occupy their positions in the alphabet for each word. For example,

// solve(["abode","ABc","xyzD"]) = [4, 3, 1]
// See test cases for more examples.

// Input will consist of alphabet characters, both uppercase and lowercase. No spaces.

export function solve(arr: string[]): number[] {
    let final_array: number[] = [];
    let letter_calculation: number = 0;

    arr.forEach(function(word) {
        for (let i = 0; i < word.length; i++) {
            if (word.toUpperCase().charCodeAt(i) == (i + 65)) {
                letter_calculation += 1;
            }
        }
    final_array.push(letter_calculation);
    letter_calculation = 0;
    });

    return final_array;
}


console.log(solve(["abode", "ABc", "xyzD"])); // expect [4, 3, 1]
console.log(solve(["IAMDEFANDJKL", "thedefgh", "xyzDEFghijabc"])); //expect [6, 5, 7]