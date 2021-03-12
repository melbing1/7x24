"use strict"

const _ = require("lodash")
const co = require("co")
const AWS = require("aws-sdk")
const lambda = new AWS.Lambda()

let invokeTarget = co.wrap(function*(target) {
  let req = {
    FunctionName: target,
    InvocationType: "RequestResponse"
  }
  let res = yield lambda.invoke(req).promise()
  console.log(res)

  if (res.FunctionError) {
    throw new Error(res.Payload)
  }

  return JSON.parse(res.Payload)
})

// expect `input` to be of shape:
// { "target": "string (lambda function to invoke)",
//   "interval": "int (seconds)",
//   "coldstarts": "int (no. of consecutive coldstarts)" }
module.exports.handler = co.wrap(function*(input, context, callback) {
  console.log(input)

  let targetName = input.target
  let output = _.clone(input)

  let res = yield invokeTarget(targetName)
  console.log(res)
  console.log(`isColdstart: ${res.isColdstart}`)

  if (!res.isColdstart) { //Technically we are acutally checking warmstarts with the "colstarts" variable
    console.log("triggered coldstart")

    output.coldstarts = (output.coldstarts || 0) + 1
	console.log(`Warmstart count: ${res.isColdstart}`)
	console.log(output.coldstarts)
    callback(null, output)
  } else {
    //console.log("not a coldstart, extending interval by 1 min")
	console.log("coldstart found, reduce interval by 1 min")
    output.interval = input.interval - 60 //subtract for the lower bound (ensure that you are starting with a very high interval in find-idle-event.json)
    output.coldstarts = 0  //Reset cold-start counter

    callback(null, output)
  }
})
