"""Mini Issue Tracker program. Originally taken from Paul Bissex's blog post:
http://news.e-scribe.com/230 and snippet: http://djangosnippets.org/snippets/28/
"""
from django.db import models
from django.conf import settings
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


STATUS_CODES = (
    (1, _('Open')),
    (2, _('Working')),
    (3, _('Closed')),
)

PRIORITY_CODES = (
    (1, _('Now')),
    (2, _('Soon')),
    (3, _('Someday')),
)


@python_2_unicode_compatible
class Ticket(models.Model):
    """Trouble tickets"""
    title = models.CharField(_('title'), max_length=100, blank=True, null=True)
    submitted_date = models.DateField(_('date submitted'), auto_now_add=True)
    modified_date = models.DateField(_('date modified'), auto_now=True)
    submitter = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_('submitter'), related_name="submitter")
    assigned_to = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_('assigned to'))
    description = models.TextField(_('description'), blank=True)
    status = models.IntegerField(_('status'), default=1, choices=STATUS_CODES)
    priority = models.IntegerField(_('priority'), default=1, choices=PRIORITY_CODES)

    class Meta:
        verbose_name = _('ticket')
        verbose_name_plural = _('tickets')
        ordering = ('status', 'priority', 'submitted_date', 'title')

    def __str__(self):
        return self.title
