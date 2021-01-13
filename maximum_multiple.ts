// Task
// Given a Divisor and a Bound , Find the largest integer N , Such That ,

// Conditions :
// N is divisible by divisor

// N is less than or equal to bound

// N is greater than 0.

// Notes
// The parameters (divisor, bound) passed to the function are only positive values .
// It's guaranteed that a divisor is Found .

export function maxMultiple(divisor: number, bound: number): number {
    let array = [];
    let array2 = []
    for (let count = 0; count < bound; count++) {
        array.push(count);
    }
    // console.log(array);
    // array.forEach(element => {
    //     if (element % divisor) {
    //         array2.push(element);
    //     }
    // });

    for (let i of array) {
        if (i % divisor == 0) {
            array2.push(i);
        }
    };

    // return array2[-1]
    return array2[array2.length -1];
}


console.log(maxMultiple(2, 7));
console.log(maxMultiple(3, 10));