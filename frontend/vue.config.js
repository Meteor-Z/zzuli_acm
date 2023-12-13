require('events').EventEmitter.defaultMaxListeners = 0;
const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  productionSourceMap: false,
  configureWebpack: config => {
    config.devtool = false;
  },
})