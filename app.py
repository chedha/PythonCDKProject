#!/usr/bin/env python3

import aws_cdk as cdk

from sample_python_cdk.sample_python_cdk_stack import SamplePythonCdkStack


app = cdk.App()
SamplePythonCdkStack(app, "sample-python-cdk")

app.synth()
