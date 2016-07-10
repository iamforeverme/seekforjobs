import * as types from "constants/actions"
import fetch from "isomorphic-fetch";
import {createAction} from "redux-actions";
import {baseURL} from 'configs';
import TimeHelper from 'libs/time-helper';
console.log(TimeHelper)
//search box
export const changeKeyword = createAction(types.CHANGE_KEYWORD, keyword => keyword);
export const changeLocation = createAction(types.CHANGE_LOCATION, location => location);
export const changePeriod = createAction(types.CHANGE_PERIOD, period => period);

export const updateJobData = createAction(types.UPDATE_JOB_DATA, data => data);
export const updateIncomeData = createAction(types.UPDATE_INCOME_DATA, data => data);

export const queryJob = () => {
    return {
        types: [types.QUERY_JOB_REQUEST, types.QUERY_JOB_SUCCESS, types.QUERY_JOB_ERROR],
        callAPI: (store) => {
            let {
                keyword,
                location,
                period
            } = store.getState().searchCondition;
            //debugger
            let end = new Date();
            let start = TimeHelper.getStartPoint(end, period);



            return fetch(`${baseURL}/analyze/count/`+
                            `${TimeHelper.format(start)}/`+
                            `${TimeHelper.format(end)}/`+
                            `${keyword||'all'}/`+
                            `${location||'all'}`)
                    .then(resp => resp.json())
                    .then(json => {
                        console.log("yangyang",json);
                        store.dispatch(updateJobData(json));
                    });

        }
    }
}

export const queryIncome = () => {
    return {
        types: [types.QUERY_INCOME_REQUEST, types.QUERY_INCOME_SUCCESS, types.QUERY_INCOME_ERROR],
        callAPI: (store) => {
            let {
                keyword,
                location,
                period
            } = store.getState().searchCondition;
            //debugger
            let end = new Date();
            let start = TimeHelper.getStartPoint(end, period);


            return fetch(`${baseURL}/analyze/salary/`+
                            `${TimeHelper.format(start)}/`+
                            `${TimeHelper.format(end)}/`+
                            `${keyword||'all'}/`+
                            `${location||'all'}`)
                    .then(resp => resp.json())
                    .then(json => {
                        console.log("yangyang",json);
                        store.dispatch(updateIncomeData(json));
                    });

        }
    }
}
