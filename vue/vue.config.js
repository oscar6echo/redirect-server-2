module.exports = {
  publicPath: './',
  css: {
    extract: true,
    loaderOptions: {
      sass: {
        data: `@import "@/styles/_variables.scss";`
      }
    }
  },

  configureWebpack: {
    output: {
      filename: '[name].js',
      chunkFilename: '[name].js'
    },
    optimization: {
      // No splitting
      //   splitChunks: false
      splitChunks: {
        cacheGroups: {
          shared: {
            test: /[\\/]node_modules[\\/]/,
            name: 'vendor',
            enforce: true,
            chunks: 'all'
          }
        }
      }
    }
  },

  chainWebpack: config => {
    if (config.plugins.has('extract-css')) {
      const extractCSSPlugin = config.plugin('extract-css');
      extractCSSPlugin &&
        extractCSSPlugin.tap(() => [
          {
            filename: '[name].css',
            chunkFilename: '[name].css'
          }
        ]);
    }
  }
};
