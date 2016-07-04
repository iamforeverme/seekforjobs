import {combineReducers} from 'redux';
import category from 'reducers/category';
import searchCondition from 'reducers/searchCondition';

const rootReducer = combineReducers({
    searchCondition
});

export default rootReducer;
