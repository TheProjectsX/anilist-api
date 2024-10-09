import requests

# GLOBALS
ANILIST_BASE_URL = "https://graphql.anilist.co"


# Format the Error from Server
def format_server_error(response: requests.Response) -> dict:
    try:
        server_result: dict = response.json()
    except Exception as e:
        return {
            "success": False,
            "message": "Internal Error occurred",
            "error": str(str(e)),
        }

    error: dict = server_result.get("errors", [{}])[0]

    return_response = {
        "success": False,
        "message": "Request Error",
        "error": error.get("message"),
        "status": error.get("status"),
    }

    if (error.get("message") == "validation") and (error.get("validation")):
        return_response["validation"] = error.get("validation")

    return return_response


"""
Function to (only) Execute the Query and Return the Result
"""


def execute_query(query, variables={}) -> dict:

    json_data = {"query": query, "variables": variables}

    response, error = None, None
    try:
        response = requests.post(ANILIST_BASE_URL, json=json_data)
    except Exception as e:
        error = e

    if not response:
        return {
            "success": False,
            "message": "Internal Error occurred",
            "error": str(error),
        }

    if not response.status_code == 200:
        return format_server_error(response)

    result: dict = response.json()
    if not result.get("data"):
        return format_server_error(response)

    return {"success": True, "data": result}
