module.exports = {
  devServer: {
    proxy: {
      '^/api': {
        target: 'http://127.0.0.1:8000',
        pathRewrite: {
          '^/api': ''
        },
        changeOrigin: true,
        secure: false,
        debug: true,
      },
    }
  },

  transpileDependencies: [
    'vuetify'
  ]
}
