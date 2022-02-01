import aws_cdk as core
import aws_cdk.assertions as assertions

from answers272312.answers272312_stack import Answers272312Stack

# example tests. To run these tests, uncomment this file along with the example
# resource in answers272312/answers272312_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = Answers272312Stack(app, "answers272312")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
