
"use strict";

let head_feedback = require('./head_feedback.js')
let body_feedback = require('./body_feedback.js')
let page = require('./page.js')
let rotate = require('./rotate.js')
let enable_torque = require('./enable_torque.js')
let walk_forward = require('./walk_forward.js')
let gait = require('./gait.js')

module.exports = {
  head_feedback: head_feedback,
  body_feedback: body_feedback,
  page: page,
  rotate: rotate,
  enable_torque: enable_torque,
  walk_forward: walk_forward,
  gait: gait,
};
