from django.conf.urls import url

from . import view

urlpatterns = [
    url(r'^hello$', view.hello),
    url(r'^testdb$', view.testdb),
    url(r'^search-post$', view.search_post),
    url(r'^add-link$', view.add_link),
    url(r'^link/(?P<link_id>\d+)$', view.link),
    url(r'^delete/(?P<link_id>\d+)$', view.delete_link),
]