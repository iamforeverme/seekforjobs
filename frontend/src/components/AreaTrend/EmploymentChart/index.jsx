import style from './employment-chart.scss';
import ReactHighcharts from 'react-highcharts';

export default class EmploymentChart extends React.Component{
    componentDidMount() {
        let chart = this.refs.chart.getChart();
        chart.series[0].addPoint({x: 10, y: 12});
    }
    render(){
        // const {
        //     jobData
        // } = this.props;

        //TEMP
        let jobData = {
            day: {
                '2016-05-01': 2,
                '2016-05-02': 4,
                '2016-05-03': 2,
                '2016-05-04': 7,
                '2016-05-05': 1
            }
        }

        let categories = [],
            data = [];

        _.map(jobData.day, (num, date) => {
            categories.push(date);
            data.push(num);
        })

        let config = {
            xAxis: {
                categories:categories
            },
            series: [{
                data: data
            }]
        };

        console.log("yangyang highchart config:", config);

        return (

            <div className={style.employmentChart}>
                <ReactHighcharts config={config} ref="chart"></ReactHighcharts>
            </div>
        );
    }
}
