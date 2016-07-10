import * as actions from "constants/actions";
import {combineReducers} from 'redux';

const defaultAreaData = {
    day: {},
    week: {},
    month: {},
    year: {}
}
export function job(state=defaultAreaData, action){
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

export function income(state=defaultAreaData, action){
    switch (action.type) {
        case actions.UPDATE_INCOME_DATA:
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

export default combineReducers({
    job,
    income
})
