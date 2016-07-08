import SearchBox from 'components/SearchBox';
import style from 'components/SearchBox/search-box.scss';
import {shallow, mount} from 'enzyme';
const expect = chai.expect;

describe('SearchBox component', () => {
    const props = {
        keyword: 'software',
        location: 'au',
        period: 'Last 1 week',
        changeHandler: sinon.spy(),
        searchHandler: sinon.spy()
    }

    it('should render a button group with 2 category buttons', () => {
        let component = shallow(<SearchBox {...props}/>);
        let btnGrp = component.find('.'+style.btnGrp);
        expect(btnGrp).to.have.length(1);
        expect(btnGrp.find('.'+style.btn)).to.have.length(2);
    })

    it('should activate/inactivate category button according to the category state', () => {
        let component = shallow(<SearchBox {...props} category="trend"/>);
        expect(component.find('#trend-btn').hasClass(style.active)).to.be.true;
        expect(component.find('#skill-btn').hasClass(style.active)).to.be.false;

        component = shallow(<SearchBox {...props} category="skill"/>);
        expect(component.find('#trend-btn').hasClass(style.active)).to.be.false;
        expect(component.find('#skill-btn').hasClass(style.active)).to.be.true;
    })

    it('should change the category state accordingly, when a category button is clicked', () => {
        let component = shallow(<SearchBox {...props} category="trend"/>);
        let trendBtn = component.find('#trend-btn');
        let skillBtn = component.find('#skill-btn');
        expect(component.state('category')).to.equal('trend');
        skillBtn.simulate('click');
        expect(component.state('category')).to.equal('skill');
        trendBtn.simulate('click');
        expect(component.state('category')).to.equal('trend');
    })

    it('should render a form with specific fields', () => {
        let component = shallow(<SearchBox {...props} category="trend"/>);
        expect(component.find('form')).to.have.length(1);
        expect(component.find('#keyword')).to.have.length(1);
        expect(component.find('#location')).to.have.length(1);
        expect(component.find('#period')).to.have.length(1);
    })

    it('should set value for form fields accroding to the state', () => {
        let component = shallow(<SearchBox {...props} category="trend"/>);
        expect(component.find('#keyword').prop('value')).to.equal(props.keyword);
        expect(component.find('#location').prop('value')).to.equal(props.location);
        expect(component.find('#period').prop('value')).to.equal(props.period);
    })

    it('should call change handler when a form field is changed', () => {
        let component = shallow(<SearchBox {...props} category="trend"/>);
        let newKeyword = 'new keyword',
            newLocation = 'new location';

        component.find('#keyword').simulate('change', {
            target: {
                value: newKeyword
            }
        });
        expect(props.changeHandler.calledWith('keyword', newKeyword)).to.be.true;

        component.find('#location').simulate('change', {
            target: {
                value: newLocation
            }
        });
        expect(props.changeHandler.calledWith('location', newLocation)).to.be.true;

        let options = component.find('#period').find('option');
        options.forEach((o) => {
            component.find('#period').simulate('change', {
                target: {
                    value: o.prop('value')
                }
            });
            expect(props.changeHandler.calledWith('period', o.prop('value'))).to.be.true;
        })
    })

    it('should call searchHandler when search button is clicked', () => {
        let component = shallow(<SearchBox {...props} />);
        component.find('.'+style.submit).simulate('click');
        expect(props.searchHandler.calledOnce).to.be.true;
    })

});
