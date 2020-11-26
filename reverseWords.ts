// Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.

// Examples
// "This is an example!" ==> "sihT si na !elpmaxe"
// "double  spaces"      ==> "elbuod  secaps"

export function reverseWords(str: string): string {
    let sentenceString: string = str;
    let stringArray: string[] = sentenceString.split(' ');
    let arrayLength = stringArray.length;
    
    let newString: string = ''

    for (let i = 0; i < arrayLength; i++) {
        let wordString: string = stringArray[i]
        let wordArray = wordString.split('')
        newString += wordArray.reverse().join('') + ' ';
    }

    return newString
}

console.log(reverseWords('The quick brown fox jumps over the lazy dog.'));
console.log(reverseWords('apple'));
console.log(reverseWords('a b c d'));
console.log(reverseWords('double  spaced  words'));