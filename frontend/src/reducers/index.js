import {combineReducers} from 'redux';
import category from 'reducers/category';
import searchCondition from 'reducers/searchCondition';
import area from 'reducers/area';

const rootReducer = combineReducers({
    searchCondition,
    area
});

export default rootReducer;
