import * as types from "constants/actions"
import fetch from "isomorphic-fetch";
import {createAction} from "redux-actions";

//search box
export const changeKeyword = createAction(types.CHANGE_KEYWORD, keyword => keyword);
export const changeLocation = createAction(types.CHANGE_LOCATION, location => location);
export const changePeriod = createAction(types.CHANGE_PERIOD, period => period);

export const queryJob = () => {
    return {
        types: [types.QUERY_JOB_REQUEST, types.QUERY_JOB_SUCCESS, types.QUERY_JOB_ERROR],
        callAPI: (store) => {
            return fetch('')
                    .then(resp => resp.json())
                    .then(json => {
                        console.log(json);
                    });
        }
    }
}
