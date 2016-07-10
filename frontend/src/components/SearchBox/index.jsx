import style from './search-box.scss';
import classnames from "utils/classnames";
import {PERIODS} from 'constants/period';

const TREND = "trend";
const SKILL = "skill";

export default class SearchBox extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            category: props.category || TREND
        }
    }
    toggleCategory(category){
        if(this.state.category === category) {
            return;
        }
        else {
            this.setState({"category": category});
        }
    }
    render() {
        const {
            keyword,
            location,
            period,
            changeHandler,
            searchHandler
        } = this.props;
        return (
            <div>
                <div className={style.btnGrp}>
                    <div id="trend-btn"
                        className={classnames(style.btn, this.state.category===TREND?style.active:"")}
                         onClick={()=>this.toggleCategory(TREND)}>
                        <i className="fa fa-line-chart"></i>
                    </div>
                    <div id="skill-btn"
                        className={classnames(style.btn, this.state.category===SKILL?style.active:"")}
                        onClick={()=>this.toggleCategory(SKILL)}>
                        <i className="fa fa-stack-exchange"></i>
                    </div>
                </div>

                <form className={style.searchBox}
                    action="" name="trend" role="form">
                    <input id="keyword" type="text"
                            className={style.input}
                            placeholder="Key words"
                            value={keyword}
                            onChange={(e) => changeHandler('keyword', e.target.value)}/>
                    <input id="location" type="text"
                            className={style.input}
                            placeholder="Location"
                            value={location}
                            onChange={(e) => changeHandler('location', e.target.value)}/>
                    <select id="period"
                            className={style.input}
                            value={period}
                            onChange={(e) => changeHandler('period', e.target.value)}>
                            {
                                _.map(PERIODS, (desc, val) => {
                                    return (
                                        <option value={val} key={val}>{desc}</option>
                                    )
                                })
                            }
                    </select>
                    <input className={style.submit}
                            defaultValue="Search"
                            onClick={() => searchHandler()}/>
                </form>

                <div className={style.slogon}>
                    <p>
                        A place
                    </p>
                    <p>
                        for a better career.
                    </p>
                </div>
            </div>
        );
    }
}
