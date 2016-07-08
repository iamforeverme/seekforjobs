import SearchBar from 'components/SearchBar';
import style from 'components/SearchBar/search-bar.scss';
import {PERIODS} from 'constants/period';
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

    it('should render a form with specific fields', () => {
        let component = shallow(<SearchBar {...props} category="trend"/>);
        expect(component.find('form')).to.have.length(1);
        expect(component.find('#searchbar-keyword')).to.have.length(1);
        expect(component.find('#searchbar-location')).to.have.length(1);
        expect(component.find('#searchbar-period')).to.have.length(1);
    })

    it('should set value for form fields accroding to the state', () => {
        let component = mount(<SearchBar {...props} category="trend"/>);
        expect(component.find('#searchbar-keyword').prop('value')).to.equal(props.keyword);
        expect(component.find('#searchbar-location').prop('value')).to.equal(props.location);
        //console.log(component.find('#searchbar-period').find('button').first().html());
        //expect(component.find('#searchbar-period').childAt(0).text()).to.equal(props.period);
    })

    it('should call change handler when a form field is changed', () => {
        let component = shallow(<SearchBar {...props} category="trend"/>);
        let newKeyword = 'new keyword',
            newLocation = 'new location';

        component.find('#searchbar-keyword').simulate('change', {
            target: {
                value: newKeyword
            }
        });
        expect(props.changeHandler.calledWith('keyword', newKeyword)).to.be.true;

        component.find('#searchbar-location').simulate('change', {
            target: {
                value: newLocation
            }
        });
        expect(props.changeHandler.calledWith('location', newLocation)).to.be.true;

        let options = component.find('#searchbar-period').find('li');
        options.forEach((o) => {
            o.simulate('click');
            _.map(PERIODS, (val, key) => {
                if(val === o.text()){
                    expect(props.changeHandler.calledWith('period', key)).to.be.true;
                }

            })
        })
    })

    it('should call searchHandler when search button is clicked', () => {
        let component = shallow(<SearchBar {...props} />);
        component.find('button').filterWhere(btn => btn.prop('type') === 'submit').simulate('click');
        expect(props.searchHandler.calledOnce).to.be.true;
    })

});
