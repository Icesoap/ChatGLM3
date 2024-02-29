# -*- coding: utf-8 -*-
import pandas as pd
import json
import requests
from typing import get_origin, Annotated
# import os
# import sys
# sys.path.append("..")

# sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from composite_demo.tool_registry import register_tool


#
#
# # class MaterialQueryPlugin:
#
# @test_start
@register_tool
def get_weather(
        city: Annotated[str, 'The material code as a param', True]
) -> pd.DataFrame:
    """
        Fetch weather data from plugin,parameter is city
    """

    # base_url = "http://localhost:8080/taskweaver/api/material_query"
    base_url = "http://4q9jeg.natappfree.cc/taskweaver/api_test"
    params = {
        "code": city,
        "name2": "test"
    }

    try:
        # Send the request and parse the response
        # response = requests.get(base_url, params=params)

        rows = []
        response = requests.post(base_url, data=json.dumps(params))

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON response
            print(response.content)
            print(response.text)
            rows.append(f"{city},{response.text}")
        else:
            print(f"code:{response.status_code}\nmessage:{response.text}")


    except Exception as e:
        raise e

    # description = (
    #     "The response is a dataframe with the following columns: content. "
    #     "The attributes column is a list of tags. "
    #     # "The price is in the format of $xx.xx."
    # )
    df = pd.DataFrame(rows, columns=["content"])
    return df
