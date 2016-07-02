import base from "./webpack.config.base.babel";
import merge from "webpack-merge";
const {
    path,
    webpack,
    UglifyJsPlugin,
    DefinePlugin
} = base.utils;

export default merge(base, {
    entry: {
        bundle: path.resolve(__dirname, "../src/index")
    },
    output: {
        path: path.resolve(__dirname, "../dist"),
        publicPath: "/dist"
    },
    plugins: [
        new DefinePlugin({
            "process.env": {
                NODE_ENV: JSON.stringify("production")
            }
        }),
        new UglifyJsPlugin({
            compress: {
                warnings: false
            }
        })
    ]
});
