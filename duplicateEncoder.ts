// The goal of this exercise is to convert a string to a new string where each character in the new string is "(" if that character appears only once in the original string, or ")" if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.

// Examples
// "din"      =>  "((("
// "recede"   =>  "()()()"
// "Success"  =>  ")())())"
// "(( @"     =>  "))((" 
// Notes

// Assertion messages may be unclear about what they display in some languages. If you read "...It Should encode XXX", the "XXX" is the expected result, not the input!

export function moreThanOnce(word: string, i: number): boolean {


    return true
}

export function duplicateEncode(word: string): string {
    let newString: string = ''

    // let splitString: string[] = word.split("");

    for (let i = 0; i < word.length; i++) {
        if (moreThanOnce(word, i) == true) {
            newString.concat(")");
        } else {
            newString.concat("(");
        }
    }

    // let letter_set: Set<string> = new Set(splitString);

    

    return newString;
}

console.log(duplicateEncode("din"));
console.log(duplicateEncode("recede"));