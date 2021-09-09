# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from typing import (
    Optional as typing___Optional,
    Text as typing___Text,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int


DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class TelemetryRecord(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    python_version: typing___Text = ...
    cli_version: typing___Text = ...
    huggingface_version: typing___Text = ...

    @property
    def imports_init(self) -> type___Imports: ...

    @property
    def imports_finish(self) -> type___Imports: ...

    @property
    def feature(self) -> type___Feature: ...

    @property
    def env(self) -> type___Env: ...

    @property
    def label(self) -> type___Labels: ...

    def __init__(self,
        *,
        imports_init : typing___Optional[type___Imports] = None,
        imports_finish : typing___Optional[type___Imports] = None,
        feature : typing___Optional[type___Feature] = None,
        python_version : typing___Optional[typing___Text] = None,
        cli_version : typing___Optional[typing___Text] = None,
        huggingface_version : typing___Optional[typing___Text] = None,
        env : typing___Optional[type___Env] = None,
        label : typing___Optional[type___Labels] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"env",b"env",u"feature",b"feature",u"imports_finish",b"imports_finish",u"imports_init",b"imports_init",u"label",b"label"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"cli_version",b"cli_version",u"env",b"env",u"feature",b"feature",u"huggingface_version",b"huggingface_version",u"imports_finish",b"imports_finish",u"imports_init",b"imports_init",u"label",b"label",u"python_version",b"python_version"]) -> None: ...
type___TelemetryRecord = TelemetryRecord

class Imports(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    torch: builtin___bool = ...
    keras: builtin___bool = ...
    tensorflow: builtin___bool = ...
    fastai: builtin___bool = ...
    sklearn: builtin___bool = ...
    xgboost: builtin___bool = ...
    catboost: builtin___bool = ...
    lightgbm: builtin___bool = ...
    pytorch_lightning: builtin___bool = ...
    pytorch_ignite: builtin___bool = ...
    transformers_huggingface: builtin___bool = ...
    jax: builtin___bool = ...
    metaflow: builtin___bool = ...

    def __init__(self,
        *,
        torch : typing___Optional[builtin___bool] = None,
        keras : typing___Optional[builtin___bool] = None,
        tensorflow : typing___Optional[builtin___bool] = None,
        fastai : typing___Optional[builtin___bool] = None,
        sklearn : typing___Optional[builtin___bool] = None,
        xgboost : typing___Optional[builtin___bool] = None,
        catboost : typing___Optional[builtin___bool] = None,
        lightgbm : typing___Optional[builtin___bool] = None,
        pytorch_lightning : typing___Optional[builtin___bool] = None,
        pytorch_ignite : typing___Optional[builtin___bool] = None,
        transformers_huggingface : typing___Optional[builtin___bool] = None,
        jax : typing___Optional[builtin___bool] = None,
        metaflow : typing___Optional[builtin___bool] = None,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"catboost",b"catboost",u"fastai",b"fastai",u"jax",b"jax",u"keras",b"keras",u"lightgbm",b"lightgbm",u"metaflow",b"metaflow",u"pytorch_ignite",b"pytorch_ignite",u"pytorch_lightning",b"pytorch_lightning",u"sklearn",b"sklearn",u"tensorflow",b"tensorflow",u"torch",b"torch",u"transformers_huggingface",b"transformers_huggingface",u"xgboost",b"xgboost"]) -> None: ...
type___Imports = Imports

class Feature(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    watch: builtin___bool = ...
    finish: builtin___bool = ...
    save: builtin___bool = ...
    offline: builtin___bool = ...
    resumed: builtin___bool = ...
    grpc: builtin___bool = ...
    metric: builtin___bool = ...
    keras: builtin___bool = ...
    sagemaker: builtin___bool = ...
    artifact_incremental: builtin___bool = ...
    metaflow: builtin___bool = ...
    prodigy: builtin___bool = ...
    set_init_name: builtin___bool = ...
    set_init_id: builtin___bool = ...
    set_init_tags: builtin___bool = ...
    set_init_config: builtin___bool = ...
    set_run_name: builtin___bool = ...
    set_run_tags: builtin___bool = ...
    set_config_item: builtin___bool = ...

    def __init__(self,
        *,
        watch : typing___Optional[builtin___bool] = None,
        finish : typing___Optional[builtin___bool] = None,
        save : typing___Optional[builtin___bool] = None,
        offline : typing___Optional[builtin___bool] = None,
        resumed : typing___Optional[builtin___bool] = None,
        grpc : typing___Optional[builtin___bool] = None,
        metric : typing___Optional[builtin___bool] = None,
        keras : typing___Optional[builtin___bool] = None,
        sagemaker : typing___Optional[builtin___bool] = None,
        artifact_incremental : typing___Optional[builtin___bool] = None,
        metaflow : typing___Optional[builtin___bool] = None,
        prodigy : typing___Optional[builtin___bool] = None,
        set_init_name : typing___Optional[builtin___bool] = None,
        set_init_id : typing___Optional[builtin___bool] = None,
        set_init_tags : typing___Optional[builtin___bool] = None,
        set_init_config : typing___Optional[builtin___bool] = None,
        set_run_name : typing___Optional[builtin___bool] = None,
        set_run_tags : typing___Optional[builtin___bool] = None,
        set_config_item : typing___Optional[builtin___bool] = None,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"artifact_incremental",b"artifact_incremental",u"finish",b"finish",u"grpc",b"grpc",u"keras",b"keras",u"metaflow",b"metaflow",u"metric",b"metric",u"offline",b"offline",u"prodigy",b"prodigy",u"resumed",b"resumed",u"sagemaker",b"sagemaker",u"save",b"save",u"set_config_item",b"set_config_item",u"set_init_config",b"set_init_config",u"set_init_id",b"set_init_id",u"set_init_name",b"set_init_name",u"set_init_tags",b"set_init_tags",u"set_run_name",b"set_run_name",u"set_run_tags",b"set_run_tags",u"watch",b"watch"]) -> None: ...
type___Feature = Feature

class Env(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    jupyter: builtin___bool = ...
    kaggle: builtin___bool = ...
    windows: builtin___bool = ...
    m1_gpu: builtin___bool = ...
    start_spawn: builtin___bool = ...
    start_fork: builtin___bool = ...
    start_forkserver: builtin___bool = ...
    start_thread: builtin___bool = ...

    def __init__(self,
        *,
        jupyter : typing___Optional[builtin___bool] = None,
        kaggle : typing___Optional[builtin___bool] = None,
        windows : typing___Optional[builtin___bool] = None,
        m1_gpu : typing___Optional[builtin___bool] = None,
        start_spawn : typing___Optional[builtin___bool] = None,
        start_fork : typing___Optional[builtin___bool] = None,
        start_forkserver : typing___Optional[builtin___bool] = None,
        start_thread : typing___Optional[builtin___bool] = None,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"jupyter",b"jupyter",u"kaggle",b"kaggle",u"m1_gpu",b"m1_gpu",u"start_fork",b"start_fork",u"start_forkserver",b"start_forkserver",u"start_spawn",b"start_spawn",u"start_thread",b"start_thread",u"windows",b"windows"]) -> None: ...
type___Env = Env

class Labels(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    code_string: typing___Text = ...
    repo_string: typing___Text = ...
    code_version: typing___Text = ...

    def __init__(self,
        *,
        code_string : typing___Optional[typing___Text] = None,
        repo_string : typing___Optional[typing___Text] = None,
        code_version : typing___Optional[typing___Text] = None,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"code_string",b"code_string",u"code_version",b"code_version",u"repo_string",b"repo_string"]) -> None: ...
type___Labels = Labels
