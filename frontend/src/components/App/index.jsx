import TitleBar from "components/TitleBar";
import Ads from "components/Ads";
import SearchBoxContainer from "containers/SearchBox";
import "styles/styles.scss";
import style from "./app.scss";
import classnames from "utils/classnames";

export default class App extends React.Component {
    render(){
        return (
            <div>
                <div className={style.navbar}>
                    <TitleBar />
                </div>
                <section
                    className={this.props.location.pathname==='/'?
                                `${style.workspace} ${style.homeBg}`:style.workspace}>
                    <div className="container">
                        <div className={style.inner}>
                            {this.props.children}
                        </div>
                    </div>
                </section>
            </div>
        );
    }
}
