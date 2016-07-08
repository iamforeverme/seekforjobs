import style from './search-bar.scss';
import 'bootstrap/js/dropdown';
import {PERIODS} from 'constants/period';

export default class SearchBar extends React.Component {
    render(){
        const {
            keyword,
            period,
            location,
            changeHandler,
            searchHandler
        } = this.props;
        return (
            <div className={style.searchBar}>
                <form className="form-inline">
                    <div className={`form-group ${style.formGrp}`}>
                        <label className="sr-only">Keywords</label>
                        <input id="searchbar-keyword"
                            className="form-control"
                            placeholder="Keywords"
                            value={keyword}
                            onChange={(e)=> changeHandler('keyword', e.target.value)}/>
                    </div>
                    <div className={`form-group ${style.formGrp}`}>
                        <label className="sr-only">Location</label>
                        <input id="searchbar-location"
                            className="form-control"
                            placeholder="Location"
                            value={location}
                            onChange={(e)=> changeHandler('location', e.target.value)}/>
                    </div>
                    <div className={`form-group ${style.formGrp}`}>
                        <div className="btn-group" id="searchbar-period">
                            <button type="button" className={`btn btn-default ${style.dropdown}`}>{period?PERIODS[period]:"Period"}</button>
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
                                    _.map(PERIODS, (decs, val) => {
                                        return (
                                            <li key={val}
                                                onClick={()=>changeHandler('period', val)}>
                                                <a href="#" >{decs}</a>
                                            </li>
                                        )
                                    })
                                }
                            </ul>
                        </div>
                    </div>
                    <button type="submit"
                            className="btn btn-default"
                            onClick={()=>searchHandler()}>Search</button>
                </form>
            </div>
        );
    }
}
