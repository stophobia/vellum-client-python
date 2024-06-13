# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

from .basic_vectorizer_intfloat_multilingual_e_5_large import BasicVectorizerIntfloatMultilingualE5Large
from .basic_vectorizer_sentence_transformers_multi_qa_mpnet_base_cos_v_1 import (
    BasicVectorizerSentenceTransformersMultiQaMpnetBaseCosV1,
)
from .basic_vectorizer_sentence_transformers_multi_qa_mpnet_base_dot_v_1 import (
    BasicVectorizerSentenceTransformersMultiQaMpnetBaseDotV1,
)
from .hkunlp_instructor_xl_vectorizer import HkunlpInstructorXlVectorizer
from .open_ai_vectorizer_text_embedding_3_large import OpenAiVectorizerTextEmbedding3Large
from .open_ai_vectorizer_text_embedding_3_small import OpenAiVectorizerTextEmbedding3Small
from .open_ai_vectorizer_text_embedding_ada_002 import OpenAiVectorizerTextEmbeddingAda002


class IndexingConfigVectorizer_TextEmbedding3Small(OpenAiVectorizerTextEmbedding3Small):
    model_name: typing.Literal["text-embedding-3-small"] = "text-embedding-3-small"

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        populate_by_name = True


class IndexingConfigVectorizer_TextEmbedding3Large(OpenAiVectorizerTextEmbedding3Large):
    model_name: typing.Literal["text-embedding-3-large"] = "text-embedding-3-large"

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        populate_by_name = True


class IndexingConfigVectorizer_TextEmbeddingAda002(OpenAiVectorizerTextEmbeddingAda002):
    model_name: typing.Literal["text-embedding-ada-002"] = "text-embedding-ada-002"

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        populate_by_name = True


class IndexingConfigVectorizer_IntfloatMultilingualE5Large(BasicVectorizerIntfloatMultilingualE5Large):
    model_name: typing.Literal["intfloat/multilingual-e5-large"] = "intfloat/multilingual-e5-large"

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        populate_by_name = True


class IndexingConfigVectorizer_SentenceTransformersMultiQaMpnetBaseCosV1(
    BasicVectorizerSentenceTransformersMultiQaMpnetBaseCosV1
):
    model_name: typing.Literal[
        "sentence-transformers/multi-qa-mpnet-base-cos-v1"
    ] = "sentence-transformers/multi-qa-mpnet-base-cos-v1"

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        populate_by_name = True


class IndexingConfigVectorizer_SentenceTransformersMultiQaMpnetBaseDotV1(
    BasicVectorizerSentenceTransformersMultiQaMpnetBaseDotV1
):
    model_name: typing.Literal[
        "sentence-transformers/multi-qa-mpnet-base-dot-v1"
    ] = "sentence-transformers/multi-qa-mpnet-base-dot-v1"

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        populate_by_name = True


class IndexingConfigVectorizer_HkunlpInstructorXl(HkunlpInstructorXlVectorizer):
    model_name: typing.Literal["hkunlp/instructor-xl"] = "hkunlp/instructor-xl"

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        populate_by_name = True


IndexingConfigVectorizer = typing.Union[
    IndexingConfigVectorizer_TextEmbedding3Small,
    IndexingConfigVectorizer_TextEmbedding3Large,
    IndexingConfigVectorizer_TextEmbeddingAda002,
    IndexingConfigVectorizer_IntfloatMultilingualE5Large,
    IndexingConfigVectorizer_SentenceTransformersMultiQaMpnetBaseCosV1,
    IndexingConfigVectorizer_SentenceTransformersMultiQaMpnetBaseDotV1,
    IndexingConfigVectorizer_HkunlpInstructorXl,
]