
// for async
import thunk from "redux-thunk";
// logger middleware
import {logger, request} from "../middlewares";

export const middlewares = [thunk, logger, request];
export const baseURL = "http://localhost:8000";
export default {
	middlewares
}
