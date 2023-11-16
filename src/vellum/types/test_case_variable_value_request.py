# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import typing_extensions

from .test_case_chat_history_variable_value_request import TestCaseChatHistoryVariableValueRequest
from .test_case_error_variable_value_request import TestCaseErrorVariableValueRequest
from .test_case_json_variable_value_request import TestCaseJsonVariableValueRequest
from .test_case_number_variable_value_request import TestCaseNumberVariableValueRequest
from .test_case_search_results_variable_value_request import TestCaseSearchResultsVariableValueRequest
from .test_case_string_variable_value_request import TestCaseStringVariableValueRequest


class TestCaseVariableValueRequest_String(TestCaseStringVariableValueRequest):
    type: typing_extensions.Literal["STRING"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class TestCaseVariableValueRequest_Number(TestCaseNumberVariableValueRequest):
    type: typing_extensions.Literal["NUMBER"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class TestCaseVariableValueRequest_Json(TestCaseJsonVariableValueRequest):
    type: typing_extensions.Literal["JSON"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class TestCaseVariableValueRequest_ChatHistory(TestCaseChatHistoryVariableValueRequest):
    type: typing_extensions.Literal["CHAT_HISTORY"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class TestCaseVariableValueRequest_SearchResults(TestCaseSearchResultsVariableValueRequest):
    type: typing_extensions.Literal["SEARCH_RESULTS"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class TestCaseVariableValueRequest_Error(TestCaseErrorVariableValueRequest):
    type: typing_extensions.Literal["ERROR"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


TestCaseVariableValueRequest = typing.Union[
    TestCaseVariableValueRequest_String,
    TestCaseVariableValueRequest_Number,
    TestCaseVariableValueRequest_Json,
    TestCaseVariableValueRequest_ChatHistory,
    TestCaseVariableValueRequest_SearchResults,
    TestCaseVariableValueRequest_Error,
]
