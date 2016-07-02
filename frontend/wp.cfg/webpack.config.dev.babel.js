import base from "./webpack.config.base.babel";
import merge from "webpack-merge";
const {path} = base.utils;

export default merge(base, {
    devtool: "cheap-source-map",
    entry: {
        bundle: path.resolve(__dirname, "../src/index")
    },
    output: {
        path: path.resolve(__dirname, "../dist"),
        publicPath: "/dist"
    }
});
