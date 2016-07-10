const msOfDay = 60 * 60 * 24 * 1000;
const msOfWeek = msOfDay * 7;
const msOfMonth = msOfDay * 30;
const msOfTriMonth = msOfMonth * 3;
const msOfYear = msOfDay * 365;

function getStartPoint(end, period){
    let start;
    switch (period) {
        case "week":
            start = end - msOfWeek;
            break;
        case "month":
            start = end - msOfMonth;
            break;
        case "tri-month":
            start = end - msOfTriMonth;
            break;
        case "year":
            start = end - msOfYear;
            break;
        default:
            start = end;
    }
    //debugger
    return new Date(start);
}

function format(msTime) {
    return msTime.toISOString().slice(0,10);
}

let TimeHelper = {
    getStartPoint,
    format
}
export default TimeHelper;
