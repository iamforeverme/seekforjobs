import {createStore, applyMiddleware} from 'redux';
import config from 'configs';
import rootReducer from 'reducers';

const
    { middlewares } = config,
    createStoreWithMiddlewares = applyMiddleware(...middlewares)(createStore),
    store = createStoreWithMiddlewares(
    rootReducer
)
export default store;
