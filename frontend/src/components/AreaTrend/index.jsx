import style from './area-trend.scss';
import SearchBarContainer from 'containers/SearchBar';
import AreaChartContainer from 'containers/AreaChart';
import LineChart from './LineChart';
import {SCALE} from 'constants/chart';

const COMMON_CONFIG = {
    credits: {
        enabled: false
    },
    legend: {
        align: 'right',
        verticalAlign: 'top',
        x: -10,
        y: 50,
        floating: true
    }
}

const JOB_CHART_CONFIG = Object.assign({}, COMMON_CONFIG, {
    yAxis: {
        title: {
            text: "Number of open jobs"
        },
        allowDecimals: false
    },
    title: {
        text: "Numbers of open jobs"
    }
});

const INCOME_CHART_CONFIG = Object.assign({}, COMMON_CONFIG, {
    yAxis: {
        title: {
            text: "Average annual salary"
        },
        allowDecimals: false
    },
    title: {
        text: "Average annual salary / $"
    }
});



export default class AreaTrend extends React.Component{
    constructor(props){
        super(props);
        this.state = {
            job_scale: this.props.job_scale,
            income_scale: this.props.income_scale
        }
    }
    changeJobScale(s){
        if(s !== this.state.scale){
            this.setState({job_scale: s});
        }
    }
    changeIncomeScale(s){
        if(s !== this.state.scale){
            this.setState({income_scale: s});
        }
    }
    render(){
        const {
            jobData,
            incomeData
        } = this.props;

        const job_config = Object.assign({}, JOB_CHART_CONFIG, {
            xAxis: {
                categories:_.map(jobData[this.state.job_scale], (num, date) => {
                                return date;
                            })
            },
            series: [{
                data: _.map(jobData[this.state.job_scale], (num, date) => {
                        return num;
                    }),
                name: null
            }]
        });

        const income_config = Object.assign({}, INCOME_CHART_CONFIG, {
            xAxis: {
                categories:_.map(incomeData[this.state.income_scale], (num, date) => {
                                return date;
                            })
            },
            series: [{
                data: _.map(incomeData[this.state.income_scale], (num, date) => {
                        return num;
                    }),
                name: null
            }]
        })

        return (
            <div>
                <SearchBarContainer />
                {/*<AreaChartContainer />*/}
                <LineChart id="job_chart"
                    config={job_config}
                    scale={this.state.job_scale}
                    onChangeScaleHandler={(s)=>{this.changeJobScale(s)}}/>
                <LineChart id="income_chart"
                    config={income_config}
                    scale={this.state.income_scale}
                    onChangeScaleHandler={(s)=>{this.changeIncomeScale(s)}}/>
            </div>
        );
    }
}


AreaTrend.defaultProps = {
    job_scale: SCALE[0],
    income_scale: SCALE[0]
}
