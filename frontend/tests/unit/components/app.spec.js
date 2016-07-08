import App from 'components/App';
import style from 'components/App/app.scss';
import TitleBar from 'components/TitleBar';
import {shallow} from 'enzyme';
const expect = chai.expect;

describe('App component', () => {
    it('should render a TitleBar and a section', () => {
        let location = {
            pathname: '/'
        }
        let component = shallow(<App location={location}/>);

        expect(component.find('TitleBar')).to.have.length(1);
        expect(component.find('section')).to.have.length(1);
    });

    it('should set a background image for the section, when current path is "/"', () => {
        let location = {
            pathname: '/'
        }
        let component = shallow(<App location={location}/>);
        expect(component.find('section').hasClass(style.homeBg)).to.be.true;
    })

    it('should NOT set a background image for the section, when current path is NOT "/"', () => {
        let location = {
            pathname: '/area'
        }
        let component = shallow(<App location={location}/>);
        expect(component.find('section').hasClass(style.homeBg)).to.be.false;
    })
})
