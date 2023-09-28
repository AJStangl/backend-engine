import logging
import json

import azure.functions as func


def main(req: func.HttpRequest, outputQueue: func.Out[str]) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        # Send the response to a queue
        outputQueue.set(json.dumps({"message": f"Hello, {name}. This HTTP triggered function executed successfully."}))

        return func.HttpResponse(
            "Input processed successfully",
            status_code=200
        )
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )