'use strict';

let isWarm = false

module.exports.test1 = (event, context, callback) => {
  if(!isWarm) {
	isWarm = true
	console.log("Cold Start")
  }


  if (event.source === 'serverless-plugin-warmup'){
	  console.log('Warming function')
	  return callback(null, 'Lambda is warm!')
  }
  
  const response = {
    statusCode: 200,
    headers: {
      'Access-Control-Allow-Origin': '*', // Required for CORS support to work
    },
    body: JSON.stringify({
      message: 'Go Serverless v1.0! Your function executed successfully!',
      input: event,
    }),
  };
  console.log('Function Running Normally')
  callback(null, response);
};
