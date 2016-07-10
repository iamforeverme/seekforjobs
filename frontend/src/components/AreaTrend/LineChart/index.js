import style from './line-chart.scss';
import ReactHighcharts from 'react-highcharts';
import {SCALE} from 'constants/chart';

export default class LineChart extends React.Component{
    render(){
        const {
            config,
            scale,
            onChangeScaleHandler
        } = this.props;
        console.log("yangyang", this.props);
        return (
            <div className={style.chartArea}>
                <ReactHighcharts className={style.lineChart}
                    config={config}></ReactHighcharts>
                    <div className={style.tools}>
                        <div className="btn-group pull-right" >
                            <button type="button" className={`btn btn-default ${style.dropdown}`}>
                                {scale}
                            </button>
                            <button type="button"
                                    className="btn btn-default dropdown-toggle"
                                    data-toggle="dropdown"
                                    aria-haspopup="true"
                                    aria-expanded="false">
                               <span className="caret"></span>
                               <span className="sr-only">Toggle Dropdown</span>
                            </button>
                            <ul className="dropdown-menu">
                                {
                                    _.map(SCALE, (s, index) => {
                                        return (
                                            <li key={index}
                                                onClick={()=>onChangeScaleHandler(s)}>
                                                <a href="#" >{s}</a>
                                            </li>
                                        )
                                    })
                                }
                            </ul>
                        </div>
                    </div>
            </div>

        );
    }
}
