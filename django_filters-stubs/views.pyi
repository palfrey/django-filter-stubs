from typing import Any, Optional

from django.views.generic import View
from django.views.generic.list import (
    MultipleObjectMixin,
    MultipleObjectTemplateResponseMixin,
)

from .constants import ALL_FIELDS as ALL_FIELDS
from .filterset import filterset_factory as filterset_factory
from .utils import MigrationNotice as MigrationNotice
from .utils import RenameAttributesBase as RenameAttributesBase

class FilterMixinRenames(RenameAttributesBase):
    renamed_attributes: Any = ...

class FilterMixin(metaclass=FilterMixinRenames):
    filterset_class: Any = ...
    filterset_fields: Any = ...
    strict: bool = ...
    def get_filterset_class(self): ...
    def get_filterset(self, filterset_class: Any): ...
    def get_filterset_kwargs(self, filterset_class: Any): ...
    def get_strict(self): ...

class BaseFilterView(FilterMixin, MultipleObjectMixin, View):
    filterset: Any = ...
    object_list: Any = ...
    def get(self, request: Any, *args: Any, **kwargs: Any): ...

class FilterView(MultipleObjectTemplateResponseMixin, BaseFilterView):
    template_name_suffix: str = ...

def object_filter(
    request: Any,
    model: Optional[Any] = ...,
    queryset: Optional[Any] = ...,
    template_name: Optional[Any] = ...,
    extra_context: Optional[Any] = ...,
    context_processors: Optional[Any] = ...,
    filter_class: Optional[Any] = ...,
): ...