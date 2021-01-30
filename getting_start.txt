1. install nodejs
2. run `npm install` in the project directory
3. change the region string in each of the files listed in files_with_region.txt
4. Deploy with `sls deploy -v`
5. Create a state machine by copying the code from `stepFunction.json` and then changing the ARN to point to the when-will-i-coldstart-dev-find-idle-timeout function deployed in your region
6. Set the permission role of the statemachine to `arn:aws:iam::340585199380:role/service-role/StepFunctions-benchmarkMachine-role-81cf677e`
7. Set the policies of the `when-will-i-coldstart-dev-{region}-lambdaRole` to
```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": "lambda:InvokeFunction",
            "Resource": "*"
        }
    ]
}
```

Next attach a second policy

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "logs:CreateLogStream",
                "cloudwatch:PutMetricData",
                "lambda:ListFunctions",
                "lambda:ListEventSourceMappings",
                "lambda:ListLayerVersions",
                "lambda:ListLayers",
                "lambda:GetAccountSettings",
                "lambda:CreateEventSourceMapping",
                "lambda:ListCodeSigningConfigs",
                "logs:CreateLogGroup",
                "logs:PutLogEvents"
            ],
            "Resource": "*"
        }
    ]
}
```

8. Run `node analysis/run.js | bunyan`
9. After the function containers have been recycled (the function finishes execution) run `node analysis/gatherResults.js | bunyan` and substrat the start and stop times to get to the idle-timeout
