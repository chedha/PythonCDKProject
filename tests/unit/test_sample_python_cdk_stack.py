import aws_cdk as core
import aws_cdk.assertions as assertions
from sample_python_cdk.sample_python_cdk_stack import SamplePythonCdkStack


def test_sqs_queue_created():
    app = core.App()
    stack = SamplePythonCdkStack(app, "sample-python-cdk")
    template = assertions.Template.from_stack(stack)

    template.has_resource_properties("AWS::SQS::Queue", {
        "VisibilityTimeout": 300
    })


def test_sns_topic_created():
    app = core.App()
    stack = SamplePythonCdkStack(app, "sample-python-cdk")
    template = assertions.Template.from_stack(stack)

    template.resource_count_is("AWS::SNS::Topic", 1)
