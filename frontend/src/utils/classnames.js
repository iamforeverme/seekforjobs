//join multi classnames
//eg, classnames('classNameA', 'classNameB') -> 'ClassNameA ClassNameB'
let classnames = (...args) => {
    //TODO: sanity check
    args.map((arg) => {
        if(arg == null)
            arg = '';
    });
    var ouput = Array.prototype.join.call(args, ' ');
    return ouput.trim();
}

export {classnames};
export default classnames;
