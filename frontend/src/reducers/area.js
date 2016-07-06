import * as actions from "constants/actions";
import {combineReducers} from 'redux';

export function job(state=[], action){
    switch (action.type) {
        case actions.UPDATE_JOB_DATA:
            if(action.error){
                return state;
            }
            else {
                return action.payload;
            }
            break;
        default:
            return state;
    }
}

export function income(state=[], action){
    switch (action.type) {
        default:
            return state;
    }
}

export default combineReducers({
    job,
    income
})
