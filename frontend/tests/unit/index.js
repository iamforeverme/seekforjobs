const expect = chai.expect;
describe('Say Hello', () => {
    let sayHi = (name) => {
        return 'Hello ' + name;
    }
    it('should say hello to react', () => {
        expect(sayHi('react')).to.equal('Hello react');
    })
});
