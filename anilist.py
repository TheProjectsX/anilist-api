from typing import Union
from components import queries, core
import json


# Get anime Filters
def getAnimeFilters():
    variables = {}

    result = core.execute_query(query=queries.ANIME_FILTERS, variables=variables)
    return result


# Filter (Search) Anime
def getFilteredAnime(
    filters: dict = {
        "search": "",
        "genres": [],
        "tags": [],
        "status": "",
        "season": None,
        "seasonYear": None,
        "isAdult": False,
        "format": None,
        "countryOfOrigin": None,
        "source": None,
        "year": None,
        "onList": None,
        "yearLesser": None,
        "yearGreater": None,
        "episodeLesser": None,
        "episodeGreater": None,
        "durationLesser": None,
        "durationGreater": None,
        "chapterLesser": None,
        "chapterGreater": None,
        "volumeLesser": None,
        "volumeGreater": None,
        "licensedBy": None,
        "isLicensed": None,
        "excludedGenres": None,
        "excludedTags": None,
        "minimumTagRank": None,
    },
    page=1,
    limit=25,
):
    """
    Function to Search / Filter Anime
    """

    variables = {**filters, "type": "ANIME", "page": page, "perPage": limit}

    result = core.execute_query(query=queries.SEARCH_QUERY, variables=variables)
    return result


# Search anime by name
def searchAnime(query, page=1, limit=25):
    variables = {"search": query, "type": "ANIME", "page": page, "perPage": limit}

    result = core.execute_query(query=queries.SEARCH_QUERY, variables=variables)
    return result


# Get Anime details by ID
def getAnimeById(id: Union[int, str]) -> dict:
    """
    Function Returns Detailed information about Anime, identified by ID
    """

    variables = {"id": id, "type": "ANIME"}

    result = core.execute_query(query=queries.ITEM_BY_ID, variables=variables)
    return result


# Get Anime Characters by ID
def getAnimeCharactersById(
    id: Union[int, str], page=1, limit=25, parse_all=False
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
            query=queries.CHARACTERS_BY_ITEM_ID, variables=variables
        )

    else:
        pass

    return result


# Get Anime Staffs by ID
def getAnimeStaffsById(id: Union[int, str], page=1, limit=25, parse_all=False) -> dict:
    """
    Function Returns Staffs Data of Anime, identified by ID

    ### Extra Argument:
    - `page` Determine which page to parse
    - `limit` Per page items
    - `parse_all` Argument is for to have all the Items in one single go or use pagination
    Values are Boolean (`True` || `False`)
    """

    if not parse_all:
        variables = {"id": id, "type": "ANIME", "page": page, "perPage": limit}

        result = core.execute_query(
            query=queries.STAFFS_BY_ITEM_ID, variables=variables
        )

    else:
        pass

    return result


# Get Anime Reviews by ID
def getAnimeReviewsById(id: Union[int, str], page=1, limit=25, parse_all=False) -> dict:
    """
    Function Returns Reviews Data of Anime, identified by ID

    ### Extra Argument:
    - `page` Determine which page to parse
    - `limit` Per page items
    - `parse_all` Argument is for to have all the Items in one single go or use pagination
    Values are Boolean (`True` || `False`)
    """

    if not parse_all:
        variables = {"id": id, "type": "ANIME", "page": page, "perPage": limit}

        result = core.execute_query(
            query=queries.REVIEWS_BY_ITEM_ID, variables=variables
        )

    else:
        pass

    return result


# Get Anime Stats by ID
def getAnimeStatsById(id: Union[int, str]) -> dict:
    """
    Function Returns Reviews Data of Anime, identified by ID
    """

    variables = {"id": id, "type": "ANIME"}

    result = core.execute_query(query=queries.STATS_BY_ITEM_ID, variables=variables)

    return result


# Get Anime Social Data by ID
def getAnimeSocialById(id: Union[int, str], page=1, limit=25, parse_all=False) -> dict:
    """
    Function Returns Social Data of Anime, identified by ID

    ### Extra Argument:
    - `page` Determine which page to parse
    - `limit` Per page items
    - `parse_all` Argument is for to have all the Items in one single go or use pagination
    Values are Boolean (`True` || `False`)
    """

    if not parse_all:
        variables = {"id": id, "page": page, "perPage": limit}

        result = core.execute_query(
            query=queries.SOCIAL_BY_ITEM_ID, variables=variables
        )

    else:
        pass

    return result


# Filter (Search) Manga
def getFilteredManga(
    filters: dict = {
        "search": "",
        "genres": [],
        "tags": [],
        "status": "",
        "season": None,
        "seasonYear": None,
        "isAdult": False,
        "format": None,
        "countryOfOrigin": None,
        "source": None,
        "year": None,
        "onList": None,
        "yearLesser": None,
        "yearGreater": None,
        "episodeLesser": None,
        "episodeGreater": None,
        "durationLesser": None,
        "durationGreater": None,
        "chapterLesser": None,
        "chapterGreater": None,
        "volumeLesser": None,
        "volumeGreater": None,
        "licensedBy": None,
        "isLicensed": None,
        "excludedGenres": None,
        "excludedTags": None,
        "minimumTagRank": None,
    },
    page=1,
    limit=25,
):
    """
    Function to Search / Filter Anime
    """

    variables = {**filters, "type": "MANGA", "page": page, "perPage": limit}

    result = core.execute_query(query=queries.SEARCH_QUERY, variables=variables)
    return result


# Get Manga details by ID
def getMangaById(id: Union[int, str]) -> dict:
    """
    Function Returns Detailed information about Manga, identified by ID
    """

    variables = {"id": id, "type": "MANGA"}

    result = core.execute_query(query=queries.ITEM_BY_ID, variables=variables)
    return result


# Get Manga Characters by ID
def getMangaCharactersById(
    id: Union[int, str], page=1, limit=25, parse_all=False
) -> dict:
    """
    Function Returns Characters Data of Manga, identified by ID

    ### Extra Argument:
    - `page` Determine which page to parse
    - `limit` Per page items
    - `parse_all` Argument is for to have all the Items in one single go or use pagination
    Values are Boolean (`True` || `False`)
    """

    if not parse_all:
        variables = {"id": id, "type": "MANGA", "page": page, "perPage": limit}

        result = core.execute_query(
            query=queries.CHARACTERS_BY_ITEM_ID, variables=variables
        )

    else:
        pass

    return result


# Get Manga Staffs by ID
def getMangaStaffsById(id: Union[int, str], page=1, limit=25, parse_all=False) -> dict:
    """
    Function Returns Staffs Data of Anime, identified by ID

    ### Extra Argument:
    - `page` Determine which page to parse
    - `limit` Per page items
    - `parse_all` Argument is for to have all the Items in one single go or use pagination
    Values are Boolean (`True` || `False`)
    """

    if not parse_all:
        variables = {"id": id, "type": "MANGA", "page": page, "perPage": limit}

        result = core.execute_query(
            query=queries.STAFFS_BY_ITEM_ID, variables=variables
        )

    else:
        pass

    return result


# Get Manga Reviews by ID
def getMangaReviewsById(id: Union[int, str], page=1, limit=25, parse_all=False) -> dict:
    """
    Function Returns Reviews Data of Manga, identified by ID

    ### Extra Argument:
    - `page` Determine which page to parse
    - `limit` Per page items
    - `parse_all` Argument is for to have all the Items in one single go or use pagination
    Values are Boolean (`True` || `False`)
    """

    if not parse_all:
        variables = {"id": id, "type": "MANGA", "page": page, "perPage": limit}

        result = core.execute_query(
            query=queries.REVIEWS_BY_ITEM_ID, variables=variables
        )

    else:
        pass

    return result


# Get Manga Stats by ID
def getMangaStatsById(id: Union[int, str]) -> dict:
    """
    Function Returns Reviews Data of Anime, identified by ID
    """

    variables = {"id": id, "type": "MANGA"}

    result = core.execute_query(query=queries.STATS_BY_ITEM_ID, variables=variables)

    return result


# Get Manga Social Data by ID
def getMangaSocialById(id: Union[int, str], page=1, limit=25, parse_all=False) -> dict:
    """
    Function Returns Social Data of Manga, identified by ID

    ### Extra Argument:
    - `page` Determine which page to parse
    - `limit` Per page items
    - `parse_all` Argument is for to have all the Items in one single go or use pagination
    Values are Boolean (`True` || `False`)
    """

    if not parse_all:
        variables = {"id": id, "page": page, "perPage": limit}

        result = core.execute_query(
            query=queries.SOCIAL_BY_ITEM_ID, variables=variables
        )

    else:
        pass

    return result


# Custom Request from User
def sendCustomRequestByQuery(query, variables):
    """
    Users can use custom query and variables to send any custom request

    `query`: parameter holds the query. User can Use built in queries from <package-name>.queries
    `variables`: variables data based on the query
    """

    result = core.execute_query(query=query, variables=variables)

    return result


# Get Character Info By ID


if __name__ == "__main__":
    print(json.dumps(getAnimeById("163134")))
