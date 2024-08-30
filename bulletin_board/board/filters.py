from django_filters import FilterSet, CharFilter

from .models import Post


class PostFilter(FilterSet):
    name = CharFilter(
        field_name='post__title',
        lookup_expr='icontains',
        label='Название объявления: '
    )
