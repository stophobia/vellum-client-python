# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import typing_extensions

from .terminal_node_chat_history_result import TerminalNodeChatHistoryResult
from .terminal_node_json_result import TerminalNodeJsonResult
from .terminal_node_search_results_result import TerminalNodeSearchResultsResult
from .terminal_node_string_result import TerminalNodeStringResult


class TerminalNodeResultOutput_String(TerminalNodeStringResult):
    type: typing_extensions.Literal["STRING"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class TerminalNodeResultOutput_Json(TerminalNodeJsonResult):
    type: typing_extensions.Literal["JSON"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class TerminalNodeResultOutput_ChatHistory(TerminalNodeChatHistoryResult):
    type: typing_extensions.Literal["CHAT_HISTORY"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class TerminalNodeResultOutput_SearchResults(TerminalNodeSearchResultsResult):
    type: typing_extensions.Literal["SEARCH_RESULTS"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


TerminalNodeResultOutput = typing.Union[
    TerminalNodeResultOutput_String,
    TerminalNodeResultOutput_Json,
    TerminalNodeResultOutput_ChatHistory,
    TerminalNodeResultOutput_SearchResults,
]
