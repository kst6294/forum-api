from rest_framework import filters

class CustomSearchFilter(filters.SearchFilter):
    def get_search_fields(self, view, request):
        if request.query_params.get('title'):
            self.search_param = "title"
            return ['title']
        if request.query_params.get('content'):
            self.search_param = "content"
            return ['content']
        return super(CustomSearchFilter, self).get_search_fields(view, request)