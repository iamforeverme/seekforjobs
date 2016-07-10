import * as actions from 'constants/actions';
import {combineReducers} from 'redux';

export function keyword(state='', action) {
    switch (action.type) {
        case actions.CHANGE_KEYWORD:
            return action.payload;
            break;
        default:
            return state;
    }
}

export function location(state='', action){
    switch (action.type) {
        case actions.CHANGE_LOCATION:
            return action.payload;
            break;
        default:
            return state;
    }
}

export function period(state='week', action){
    switch (action.type) {
        case actions.CHANGE_PERIOD:
            return action.payload;
            break;
        default:
            return state;
    }
}

const searchCondition = combineReducers({
    keyword,
    location,
    period
});
export default searchCondition;
