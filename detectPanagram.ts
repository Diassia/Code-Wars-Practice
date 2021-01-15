// A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).

// Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.

    // use regex replace all (to replace spaces/punctuation with nothing)
    // lower case string
    // put in a set (remove duplicates)
    // count length of string (if 26, return true)

export function isPangram(phrase: string): boolean {
    let newString: Set<string> = new Set((phrase.replace(/\W|\d/g, '')).toLowerCase());
    if (newString.size == 26) {
        return true;
    } else {
        return false;
    }
    
    // console.log(newString);

    // return true;
}

console.log(isPangram("The quick brown fox jumps over the lazy dog."));
console.log(isPangram("This is not a pangram."));