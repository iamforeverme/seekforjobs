import TimeHelper from 'libs/time-helper';
const expect = chai.expect;

describe('TimeHelper lib', () => {
    it('should calculate start time by given end time and period', () => {
        let end = new Date(1468122953118);
        let period = "week";
        let start = TimeHelper.getStartPoint(end, 'week');
        expect(end.toISOString().slice(8, 10) - start.toISOString().slice(8, 10))
            .to.equal(7);
    })
})
