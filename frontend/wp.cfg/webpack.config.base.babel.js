import webpack from "webpack";
import path from "path";
const
    {CommonsChunkPlugin, UglifyJsPlugin} = webpack.optimize,
    {ProvidePlugin, DefinePlugin} = webpack;

export default {
    entry: {
        common: ["react", "react-dom", "lodash"]
    },
    output: {
        filename: "[name].js",
        chunkFilename: "[id].chunk.js"
    },
    module: {
        loaders: [{
            test   : /\.jsx?$/,
            loaders: [
                "react-hot",
                "babel?presets[]=react,presets[]=es2015,presets[]=stage-0"
            ],
            exclude: /node_modules/
        }, {
            test  : /\.s[ac]ss$/,
            loader: "style!css?module&localIdentName=[name]__[local]__[hash:base64:10]!sass",
            exclude: /node_modules/
        }, {
            test  : /\.(jpe?g|svg|png)$/,
            loader: "url?limit=10000&name=/images/[hash:20].[ext]",
            exclude: /node_modules/
        }]
    },
    sassLoader: {
        includePaths: [path.resolve(__dirname, "../src")]
    },
    resolve: {
        extensions: [".jsx", ".js", ".scss", ""],
        root  : [
            path.resolve(__dirname, "../src")
        ]
    },
    plugins: [
        new webpack.NoErrorsPlugin(),
        new webpack.ProvidePlugin({
            React   : "react",
            ReactDOM: "react-dom",
            _       : "lodash"
        })
    ],
    /*********** utils ************/
    utils: {
        webpack,
        path,
        CommonsChunkPlugin,
        UglifyJsPlugin,
        ProvidePlugin,
        DefinePlugin
    }
}
