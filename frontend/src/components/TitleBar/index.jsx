import style from "./title-bar.scss";
import classnames from "utils/classnames";
import {Link} from 'react-router';

export default class TitleBar extends React.Component{
    render() {
        return (
            <div className="container">
                <ul className={style.nav}>
                    <li className={style.navTab}>
                        <Link to="/" className={style.link}>
                            Home
                        </Link>
                    </li>                    
                    <li className={style.navTab}>
                        <Link to={'/area'} className={style.link}>
                        <i className="fa fa-line-chart"></i>
                        {" "}Area trend
                        </Link>
                    </li>
                    <li className={style.navTab}>
                        <i className="fa fa-stack-exchange"></i>
                        {" "}Skill stack
                    </li>
                </ul>
            </div>

        );
    }
}
