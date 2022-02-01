# testing CDK and Sam local invoke with layers

Please note layer commons with python subpath as mention in doc :
https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html

# Testing 

as per doc 
https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-cdk-getting-started.html

cdk synth --no-staging

sam local invoke answers272312testfunctionXXXXXX --no-event -t ./cdk.out/Answers272312Stack.template.json

