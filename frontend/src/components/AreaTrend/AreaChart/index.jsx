import style from './area-chart.scss';

export default class AreaChart extends React.Component{
    constructor(props){
        super(props);

    }
    drawRegionsMap() {
        console.log('draw', this);
        if(!google.visualization)
            return;
        let data = google.visualization.arrayToDataTable([
          ['State', 'Popularity'],
          ['Queensland', 200]
        ]);

        let options = {
          region: 'AU',
          displayMode: 'regions',
          resolution: 'provinces',
        };
        if(!this.chart){
            this.chart = new google.visualization.GeoChart(document.getElementById('regions_div'));
        }
        this.chart.draw(data, options);
    }
    componentDidMount(){
        console.log('mount', this);
        google.charts.load('current', {'packages':['geochart']});
        google.charts.setOnLoadCallback(() => this.drawRegionsMap());
    }
    render(){
        console.log('render', this);
        this.drawRegionsMap();
        return (
            <div className={style.areaChart}>
                <div id="regions_div" className={style.map}>

                </div>
                <div className={style.static}>
                </div>

            </div>
        );
    }
}
