const CopyWebpackPlugin = require('copy-webpack-plugin');
const { defineConfig } = require('@vue/cli-service');
module.exports = defineConfig({
  transpileDependencies: true,
  productionSourceMap: false,
  devServer: {
    allowedHosts: "all"
  },
  configureWebpack: config => {
    config.devtool = false;
    config.plugins.push(
      new CopyWebpackPlugin({
        patterns: [
          {
            from: 'config.js',
            to: 'config.js',
          },
        ],
      })
    );
  }
})