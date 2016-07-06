import style from './area-trend.scss';
import SearchBarContainer from 'containers/SearchBar';
import AreaChart from './AreaChart';
import EmploymentChart from './EmploymentChart';
import IncomeChart from './IncomeChart';


export default class AreaTrend extends React.Component{
    render(){
        return (
            <div>
                <SearchBarContainer />
                <AreaChart />
                <EmploymentChart />
                <IncomeChart />
            </div>
        );
    }
}
