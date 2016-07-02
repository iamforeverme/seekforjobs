import {Provider} from "react-redux";
import store from "store";
import App from "containers/App";


ReactDOM.render(
    <Provider {...{store}}>
        <App />
    </Provider>
    ,
    document.getElementById("my-app")
)
