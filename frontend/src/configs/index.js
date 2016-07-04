
// for async
import thunk from "redux-thunk";
// logger middleware
import {logger/*, request*/} from "../middlewares";

export const middlewares = [thunk, logger/*, request*/];
export default {
	middlewares
}
