// The goal of this exercise is to convert a string to a new string where each character in the new string is "(" if that character appears only once in the original string, or ")" if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.

// Examples
// "din"      =>  "((("
// "recede"   =>  "()()()"
// "Success"  =>  ")())())"
// "(( @"     =>  "))((" 
// Notes

// Assertion messages may be unclear about what they display in some languages. If you read "...It Should encode XXX", the "XXX" is the expected result, not the input!

export function moreThanOnce(word: string, letterTest: string): boolean {
    let count = 0;
    for (let index = 0; index < word.length; index++) {
        if (word[index].toLowerCase() == letterTest) {
            count += 1
        }
    }

    if (count > 1) {
        return true
    } else {
        return false
    }
}

export function duplicateEncode(word: string): string {
    let newString: string = "";

    for (let i = 0; i < word.length; i++) {
        let letterTest = word[i].toLowerCase();
        if (moreThanOnce(word, letterTest) == true) {
            newString += ")";
        } else {
            newString += "(";
        }
    }
 
    return newString;
}

console.log(duplicateEncode("din"));
console.log(duplicateEncode("recede"));
console.log(duplicateEncode("Success"));