'use strict'
const merge = require('webpack-merge')
const prodEnv = require('./prod.env')

module.exports = merge(prodEnv, {
  NODE_ENV: '"development"',
  //ROOT_API: '"https://sms.gitwork.ru"',
  ROOT_API: '"http://localhost:8000"'
})
