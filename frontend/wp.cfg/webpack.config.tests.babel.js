import base from "./webpack.config.base.babel";
import merge from "webpack-merge";
const {
    webpack,
    path,
    CommonsChunkPlugin,
    ProvidePlugin
} = base.utils;

export default merge(base, {
    devtool: "source-map",
    entry: {
        bundle: "mocha!./tests/unit/index",
        tests : ["chai", "react-addons-test-utils", "enzyme", "sinon/pkg/sinon"]
    },
    output: {
        path: path.resolve(__dirname, "tests/unit"),
        publicPath: "/"
    },
    module: {
        noParse: [
            /sinon/
        ]
    },
    plugins: [
        new ProvidePlugin({
            chai     : "chai",
            enzyme   : "enzyme",
            TestUtils: "react-addons-test-utils",
            sinon    : "sinon/pkg/sinon"
        })
    ],
    externals: {
        "cheerio": "window",
        'react/addons': true,
        "react/lib/ExecutionEnvironment": true,
        "react/lib/ReactContext": true
    }
});
