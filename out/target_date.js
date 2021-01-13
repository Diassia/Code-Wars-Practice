"use strict";
// You have an amount of money a0 > 0 and you deposit it with a constant interest rate of p% > 0 per year on the 1st of January 2016. You want to have an amount a >= a0.
Object.defineProperty(exports, "__esModule", { value: true });
exports.dateNbDays = void 0;
// Task:
// The function date_nb_days (or dateNbDays...) with parameters a0, a, p will return, as a string, the date on which you have just reached a.
// Example:
// date_nb_days(100, 101, 0.98) --> "2017-01-01" (366 days)
// date_nb_days(100, 150, 2.00) --> "2035-12-26" (7299 days)
// Notes:
// The return format of the date is "YYYY-MM-DD"
// The deposit is always on the "2016-01-01"
// If p% is the rate for a year the rate for a day is p divided by 36000 since banks consider that there are 360 days in a year.
// You have: a0 > 0, p% > 0, a >= a0
// a0 > 0 (amount of money)
// p% > 0 (constant interest rate per year)
// a >= a0 (the amount you want to have)
function padNumber(number) {
    if (number < 10) {
        return "0" + number.toString();
    }
    else {
        return number.toString();
    }
}
// export function pad_date(finalDate) {
//     let padded_date = ''
//     const year = finalDate.getFullYear();
//     const month = finalDate.getMonth();
//     const day = finalDate.getDate();
//     return padded_date
// }
function dateNbDays(a0, a, p) {
    var string = '';
    var interestPerDay = p / 36000;
    var dayCount = 0;
    for (var count = a0; count <= a; count += (interestPerDay * count)) {
        console.log("This is day " + dayCount + (". Your count is " + count));
        dayCount += 1;
    }
    ;
    console.log(dayCount);
    var depositDate = new Date("2016-01-01");
    console.log(depositDate);
    // depositDate.toISOString();
    var year = depositDate.getFullYear();
    var month = depositDate.getMonth();
    var day = depositDate.getDate();
    var finalDate = new Date(year, month, day + dayCount);
    // let month_string = month.toString();
    // if (month_string.length <= 1) {
    //     pad_date(finalDate);
    // }
    // const year_final = finalDate.getFullYear();
    // const month_final = 
    // const day_final = ;
    var new_month = padNumber(finalDate.getMonth() + 1);
    var new_day = padNumber(finalDate.getDate());
    var formatted_date = finalDate.getFullYear() + "-" + new_month + "-" + new_day;
    return formatted_date;
}
exports.dateNbDays = dateNbDays;
console.log(dateNbDays(100, 101, 0.98));
console.log(dateNbDays(4281, 5087, 2));
//# sourceMappingURL=target_date.js.map