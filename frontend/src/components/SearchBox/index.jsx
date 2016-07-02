import style from './search-box.scss';
import classnames from "utils/classnames";

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
        return (
            <div>
                <div className={style.btnGrp}>
                    <div className={classnames(style.btn, this.state.category===TREND?style.active:"")}
                         onClick={()=>this.toggleCategory(TREND)}>
                        <i className="fa fa-line-chart"></i>
                    </div>
                    <div className={classnames(style.btn, this.state.category===SKILL?style.active:"")}
                        onClick={()=>this.toggleCategory(SKILL)}>
                        <i className="fa fa-stack-exchange"></i>
                    </div>
                </div>

                <form className={style.searchBox}
                    action="" name="trend" role="form">
                    <input id="keyword" type="text"
                            className={style.input}
                            placeholder="Key words"/>
                    <input id="location" type="text"
                            className={style.input}
                            placeholder="Location"/>
                    <input id="period" type="text"
                            className={style.input}
                            placeholder="Period"/>
                    <input className={style.submit}
                        type="submit" value="Search"/>
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
