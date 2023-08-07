from constructs import Construct
from aws_cdk import (
    Duration,
    Stack,
    aws_iam as iam,
    aws_sqs as sqs,
    aws_sns as sns,
    aws_sns_subscriptions as subs,
    aws_lambda as _lambda,
    aws_apigateway as apigw,
    aws_s3 as s3
)

from hitcounter import HitCounter


class SamplePythonCdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # bucket = s3.Bucket(self, "mySpecialBucket-62477")

        my_lambda = _lambda.Function(
            self, "HelloHandler",
            runtime=_lambda.Runtime.PYTHON_3_9,
            code=_lambda.Code.from_asset("lambda"),
            handler="hello.handler"
        )

        hello_with_counter = HitCounter(
            self, "HelloHitCounter",
            downstream=my_lambda,
        )

        apigw.LambdaRestApi(
            self, "Endpoint",
            handler=hello_with_counter.handler,
        )

        # queue = sqs.Queue(
        #     self, "SamplePythonCdkQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )
        #
        # topic = sns.Topic(
        #     self, "SamplePythonCdkTopic"
        # )
        #
        # topic.add_subscription(subs.SqsSubscription(queue))
