curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{
    "resource": "/",
    "path": "/cast",
    "httpMethod": "GET",
    "queryStringParameters": {
    },
    "multiValueQueryStringParameters":{
    },
    "pathParameters": {
    },
    "requestContext": {
      "accountId": "12345678912",
      "resourceId": "foobar",
      "stage": "testStage",
      "requestId": "deef124878-7910-11e6-8f14-25afc3e9ae33",
      "resourcePath": "/",
      "httpMethod": "GET",
      "apiId": "gy415nuibcd"
    },
    "body": "{}",
    "isBase64Encoded": false
}'