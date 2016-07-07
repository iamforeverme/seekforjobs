import style from './employment-chart.scss';
import ReactHighcharts from 'react-highcharts';

export default class EmploymentChart extends React.Component{
    componentDidMount() {
        let chart = this.refs.chart.getChart();
        chart.series[0].addPoint({x: 10, y: 12});
    }
    render(){
        const {
            job
        } = this.props;
        console.log("yangyang job", job);

        let categories = _.map(job.day, (num, date) => {
            return date;
        });
        let data = _.map(job.day, (num, date) => {
            return num;
        });
        // var config = {
        //     xAxis: {
        //         categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        //     },
        //     series: [{
        //         data: [29.9, 71.5, 106.4, 129.2, 144.0, 176.0, 135.6, 148.5, 216.4, 194.1, 295.6, 454.4]
        //     }]
        // };

        let config = {
            xAxis: {
                categories:categories
            },
            series: [{
                data: data
            }]
        };

        console.log("yangyang", config);

        return (

            <div className={style.employmentChart}>
                <ReactHighcharts config={config} ref="chart"></ReactHighcharts>
            </div>
        );
    }
}
