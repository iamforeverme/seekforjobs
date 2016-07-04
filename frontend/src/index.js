import {Provider} from "react-redux";
import store from "store";
import App from "containers/App";
import Routes from "components/Routes";
console.log(Routes);

ReactDOM.render(
    <Provider {...{store}}>
        <Routes />
    </Provider>
    ,
    document.getElementById("my-app")
)
