import style from './area-trend.scss';
import SearchBar from 'components/SearchBar';
import AreaChart from './AreaChart';
import EmploymentChart from './EmploymentChart';
import IncomeChart from './IncomeChart';


export default class AreaTrend extends React.Component{
    render(){
        return (
            <div>
                <SearchBar />
                <AreaChart />
                <EmploymentChart />
                <IncomeChart />
            </div>
        );
    }
}
