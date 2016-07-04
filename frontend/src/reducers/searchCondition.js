import * as actions from 'constants/actions';

export default function keyword(state='all', action) {
    switch (action.type) {
        case actions.CHANGE_KEYWORD:
            return action.payload;
            break;
        default:
            return state;
    }
}

export default function location(state='all', action){
    switch (action.type) {
        case actions.CHANGE_LOCATION:
            return action.payload;
            break;
        default:
            return state;
    }
}

export default function period(state='week', action){
    switch (action.type) {
        case actions.CHANGE_PERIOD:
            return action.payload;
            break;
        default:
            return state;
    }
}
