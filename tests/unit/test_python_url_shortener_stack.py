import aws_cdk as core
import aws_cdk.assertions as assertions

from python_url_shortener.python_url_shortener_stack import PythonUrlShortenerStack

# example tests. To run these tests, uncomment this file along with the example
# resource in python_url_shortener/python_url_shortener_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = PythonUrlShortenerStack(app, "python-url-shortener")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
