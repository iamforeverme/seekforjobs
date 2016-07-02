import {createStore, applyMiddleware} from 'redux';
import config from 'configs';
import rootReducer from 'reducers';

const store = createStore(
    rootReducer
)
console.log(store);
export default store;
