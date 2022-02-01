from aws_cdk import (
    Stack,
    aws_lambda as lambda_,
    Duration
)
from constructs import Construct

class Answers272312Stack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        commons_layer = lambda_.LayerVersion(self, "commons_layer",
        code=lambda_.Code.from_asset("app/layers/commons/"),
        compatible_runtimes=[lambda_.Runtime.PYTHON_3_9]
        )

        lambda_.Function(self, "answers272312_testfunction",
        code=lambda_.Code.from_asset("app/lambda_functions/"),
        runtime=lambda_.Runtime.PYTHON_3_9,
        timeout=Duration.minutes(1),
        handler="test_function.lambda_handler",
        layers=[commons_layer]
)
