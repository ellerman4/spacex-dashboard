# Middleware to inject two more headers - the generic Report-To and NEL for network error logging
from dotenv import load_dotenv
import os
load_dotenv()

class ReportUriMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        # Header values from https://report-uri.com/account/setup/
        response["Report-To"] = str(os.getenv('Report-To'))     # include in .env variable
        response["NEL"] = str(os.getenv('NEL'))     # include in .env variable
        return response