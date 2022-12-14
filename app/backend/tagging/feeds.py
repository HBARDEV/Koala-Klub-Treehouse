from django.contrib.sites.shortcuts import get_current_site
from django.contrib.syndication.views import Feed
from django.utils.translation import gettext as _

import tagging


class LatestCommentFeed(Feed):
    """Feed of latest comments on the current site."""

    def __call__(self, request, *args, **kwargs):
        self.site = get_current_site(request)
        return super().__call__(request, *args, **kwargs)

    def title(self):
        return _("%(site_name)s comments") % dict(site_name=self.site.name)

    def link(self):
        return "http://%s/" % (self.site.domain)

    def description(self):
        return _("Latest comments on %(site_name)s") % dict(site_name=self.site.name)

    def items(self):
        qs = tagging.get_model().objects.filter(
            site__pk=self.site.pk,
            is_public=True,
            is_removed=False,
        )
        return qs.order_by('-submit_date')[:40]

    def item_pubdate(self, item):
        return item.submit_date
