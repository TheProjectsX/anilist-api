from typing import List, TypedDict, Optional


class AnimeFilterOptionTypes(TypedDict, total=False):
    page: Optional[int]  # Defaults to 1
    perPage: Optional[int]  # Defaults to 25
    id: Optional[int]
    type: Optional[str]  # Could be MediaType (custom type)
    isAdult: Optional[bool]  # Defaults to False
    search: Optional[str]
    format: Optional[List[str]]  # Could be List[MediaFormat] (custom type)
    status: Optional[str]  # Could be MediaStatus (custom type)
    countryOfOrigin: Optional[str]  # Could be CountryCode (custom type)
    source: Optional[str]  # Could be MediaSource (custom type)
    season: Optional[str]  # Could be MediaSeason (custom type)
    seasonYear: Optional[int]
    year: Optional[str]
    onList: Optional[bool]
    yearLesser: Optional[int]  # Could be FuzzyDateInt (custom type)
    yearGreater: Optional[int]  # Could be FuzzyDateInt (custom type)
    episodeLesser: Optional[int]
    episodeGreater: Optional[int]
    durationLesser: Optional[int]
    durationGreater: Optional[int]
    chapterLesser: Optional[int]
    chapterGreater: Optional[int]
    volumeLesser: Optional[int]
    volumeGreater: Optional[int]
    licensedBy: Optional[List[int]]
    isLicensed: Optional[bool]
    genres: Optional[List[str]]
    excludedGenres: Optional[List[str]]
    tags: Optional[List[str]]
    excludedTags: Optional[List[str]]
    minimumTagRank: Optional[int]
    sort: Optional[List[str]]


AnimeFilterOptions: AnimeFilterOptionTypes = {
    "page": 1,
    "perPage": 25,
    "id": None,
    "type": None,
    "isAdult": False,
    "search": None,
    "format": None,
    "status": None,
    "countryOfOrigin": None,
    "source": None,
    "season": None,
    "seasonYear": None,
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
    "genres": None,
    "excludedGenres": None,
    "tags": None,
    "excludedTags": None,
    "minimumTagRank": None,
    "sort": ["POPULARITY_DESC", "SCORE_DESC"],
}
