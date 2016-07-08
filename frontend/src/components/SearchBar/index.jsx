import style from './search-bar.scss';
import 'bootstrap/js/dropdown';

export default class SearchBar extends React.Component {
    render(){
        const {
            keyword,
            period,
            location
        } = this.props;
        console.log(this.props);
        return (
            <div className={style.searchBar}>
                <form className="form-inline">
                    <div className={`form-group ${style.formGrp}`}>
                        <label className="sr-only">Keywords</label>
                        <input className="form-control"
                            placeholder="Keywords"
                            value={keyword}/>
                    </div>
                    <div className={`form-group ${style.formGrp}`}>
                        <label className="sr-only">Location</label>
                        <input className="form-control"
                            placeholder="Location"
                            value={location}/>
                    </div>
                    <div className={`form-group ${style.formGrp}`}>
                        <div className="dropdown">
                            <button className="btn btn-default dropdown-toggle"
                                type="button"
                                data-toggle="dropdown"
                                aria-haspopup="true"
                                aria-expanded="true">{period?period:"Period"}
                                <span class="caret"></span>
                            </button>
                            <ul className="dropdown-menu">
                                <li><a href="#">Last 1 week</a></li>
                                <li><a href="#">Last 1 month</a></li>
                                <li><a href="#">Last 3 months</a></li>
                                <li><a href="#">Last 1 year</a></li>
                            </ul>
                        </div>
                    </div>
                    <button type="submit" className="btn btn-default">Search</button>
                </form>
            </div>

            // <form className={style.searchBar}
            //     action="" name="trend" role="form">
            //     <input id="keyword" type="text"
            //             className={style.input}
            //             placeholder="Key words"
            //             value={keyword}/>
            //     <input id="location" type="text"
            //             className={style.input}
            //             placeholder="Location"
            //             value={location}/>
            //     <select id="period"
            //             className={style.input}
            //             value={period}>
            //              <option value="week">last 1 week</option>
            //              <option value="month">last 1 month</option>
            //              <option value="tri-month">last 3 months</option>
            //              <option value="year">last 1 year</option>
            //     </select>
            // </form>

        );
    }
}
