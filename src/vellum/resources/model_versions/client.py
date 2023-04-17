# This file was auto-generated by Fern from our API Definition.

import urllib.parse
import uuid
from json.decoder import JSONDecodeError

import httpx
import pydantic

from ...core.api_error import ApiError
from ...core.remove_none_from_headers import remove_none_from_headers
from ...environment import VellumEnvironment
from .types.model_version_read import ModelVersionRead


class ModelVersionsClient:
    def __init__(self, *, environment: VellumEnvironment = VellumEnvironment.PRODUCTION, api_key: str):
        self._environment = environment
        self.api_key = api_key

    def retrieve(self, model_version_id: uuid.UUID) -> ModelVersionRead:
        _response = httpx.request(
            "GET",
            urllib.parse.urljoin(f"{self._environment.default}/", f"v1/model-versions/{model_version_id}"),
            headers=remove_none_from_headers({"X-API-KEY": self.api_key}),
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ModelVersionRead, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncModelVersionsClient:
    def __init__(self, *, environment: VellumEnvironment = VellumEnvironment.PRODUCTION, api_key: str):
        self._environment = environment
        self.api_key = api_key

    async def retrieve(self, model_version_id: uuid.UUID) -> ModelVersionRead:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "GET",
                urllib.parse.urljoin(f"{self._environment.default}/", f"v1/model-versions/{model_version_id}"),
                headers=remove_none_from_headers({"X-API-KEY": self.api_key}),
            )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ModelVersionRead, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)