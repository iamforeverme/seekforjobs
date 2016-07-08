import TitleBar from 'components/TitleBar';
import {shallow} from 'enzyme';
import style from 'components/TitleBar/title-bar.scss';
const expect = chai.expect;

describe('TitleBar component', () => {
    it('should render a list with 3 li', () => {
        let component = shallow(<TitleBar />);
        expect(component.find('ul')).to.have.length(1);
        expect(component.find('li')).to.have.length(3);
    })
})
