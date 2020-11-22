// We want an array, but not just any old array, an array with contents!

// Write a function that produces an array with the numbers 0 to N-1 in it.

// For example, the following code will result in an array containing the numbers 0 to 4:

// arr(5) // => [0,1,2,3,4]

function range(start: number, end: number) : number[] {
    let array = []
    for(let i = start; i <= end; i++) {
        array.push(i);
    }
    return array
}

export const arr = (n: number = 0): number[] => {
    let range_array = range(0, (n - 1))
    return range_array;
};

console.log(arr(10));

// CodeWars solution:
//     xport const arr = (n = 0): number[] => Array.from({length: n}, (_, i) => i);