from typing import Union
from components import queries, core
import json


# Get Anime details by ID
def getAnimeById(id: Union[int, str]) -> dict:
    """
    Function Returns Detailed information about Anime, identified by ID
    """

    variables = {"id": id, "type": "ANIME"}

    result = core.execute_query(query=queries.ANIME_BY_ID, variables=variables)
    return result


# Get Anime Characters by ID
def getAnimeCharactersById(
    id: Union[int, str], page=1, limit=25, parse_all=True
) -> dict:
    """
    Function Returns Characters Data of Anime, identified by ID

    ### Extra Argument:
    - `page` Determine which page to parse
    - `limit` Per page items
    - `parse_all` Argument is for to have all the Items in one single go or use pagination
    Values are Boolean (`True` || `False`)
    """

    if not parse_all:
        variables = {"id": id, "type": "ANIME", "page": page, "perPage": limit}

        result = core.execute_query(
            query=queries.CHARACTERS_BY_ANIME_ID, variables=variables
        )

    else:
        pass

    return result


if __name__ == "__main__":
    print(json.dumps(getAnimeCharactersById(166531)))
