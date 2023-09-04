# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import typing_extensions

from .templating_node_chat_history_result import TemplatingNodeChatHistoryResult
from .templating_node_json_result import TemplatingNodeJsonResult
from .templating_node_search_results_result import TemplatingNodeSearchResultsResult
from .templating_node_string_result import TemplatingNodeStringResult


class TemplatingNodeResultOutput_String(TemplatingNodeStringResult):
    type: typing_extensions.Literal["STRING"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class TemplatingNodeResultOutput_Json(TemplatingNodeJsonResult):
    type: typing_extensions.Literal["JSON"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class TemplatingNodeResultOutput_ChatHistory(TemplatingNodeChatHistoryResult):
    type: typing_extensions.Literal["CHAT_HISTORY"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class TemplatingNodeResultOutput_SearchResults(TemplatingNodeSearchResultsResult):
    type: typing_extensions.Literal["SEARCH_RESULTS"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


TemplatingNodeResultOutput = typing.Union[
    TemplatingNodeResultOutput_String,
    TemplatingNodeResultOutput_Json,
    TemplatingNodeResultOutput_ChatHistory,
    TemplatingNodeResultOutput_SearchResults,
]