import AppContainer from "containers/App";
import SearchBoxContainer from 'containers/SearchBox';
import AreaTrend from 'components/AreaTrend';
import {Router, Route, IndexRoute, Link, browserHistory} from 'react-router';

class Routes extends React.Component {
    render() {
        return (
            <Router history={browserHistory}>
                <Route path="/" component={AppContainer}>
                    <IndexRoute component={SearchBoxContainer} />
                    {/*<Route path="area" getComponent={
                        (location, cb) => {
                            require.ensure([], (require) => {
                                cb(null, require('components/AreaTrend').default);
                            }, "area");
                        }
                    } />*/}
                    <Route path="area" component={AreaTrend} />
                </Route>
            </Router>
        );
    }
}

export default Routes;
