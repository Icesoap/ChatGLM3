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

# from composite_demo import tool_registry


# _TOOL_DESCRIPTIONS = tool_registry._TOOL_DESCRIPTIONS
#
#
# def test_start(func: callable):
#     print(f'material_query------:{_TOOL_DESCRIPTIONS}')
#     print("test_start")

# import sys
# print(sys.path)

if __name__ == '__main__':
    print("material_test")


#
#
# # class MaterialQueryPlugin:
#
# @test_start
@register_tool
def get_material(
        material_code: Annotated[str, 'The material code as a param', True]
) -> pd.DataFrame:
    """
        Fetch material data from plugin,parameter is material_code
    """

    # base_url = "http://localhost:8080/taskweaver/api/material_query"
    base_url = "http://4q9jeg.natappfree.cc/taskweaver/api/material_query"
    params = {
        "code": material_code,
        "name2": "test"
    }

    try:
        # Send the request and parse the response
        # response = requests.get(base_url, params=params)

        rows = []
        # response = requests.post(base_url, data=json.dumps(params))
        # response = requests.get(base_url, params=params)
        response = requests.post(base_url, data=json.dumps(params))

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON response
            print(f'plugin-content----------:{response.content}')
            print(f'plugin-text----------:{response.text}')
            rows.append(f"{material_code},{response.text}")
        else:
            print(f"code:{response.status_code}\nmessage:{response.text}")


    except Exception as e:
        raise e

    description = (
        "The response is a dataframe with the following columns: content. "
        "The attributes column is a list of tags. "
        # "The price is in the format of $xx.xx."
    )
    df = pd.DataFrame(rows, columns=["content"])
    return df
