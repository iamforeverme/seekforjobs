import style from './area-trend.scss';
import SearchBarContainer from 'containers/SearchBar';
import AreaChartContainer from 'containers/AreaChart';
import EmploymentChartContainer from 'containers/EmploymentChart';
import IncomeChart from './IncomeChart';


export default class AreaTrend extends React.Component{
    render(){
        return (
            <div>
                <SearchBarContainer />
                {/*<AreaChartContainer />*/}
                <EmploymentChartContainer />
                <IncomeChart />
            </div>
        );
    }
}
