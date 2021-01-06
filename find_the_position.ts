// When provided with a letter, return its position in the alphabet.

// Input :: "a"

// Ouput :: "Position of alphabet: 1"

export function position(alphabet:string):string {
    let alphabet_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'];
    return "Position of alphabet: " + (alphabet_list.indexOf(alphabet) +1);
}

console.log(position("a"))