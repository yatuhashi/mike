from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from mike.lib.mike_object import MikeObject
from mike.lib.objects.switch import Switch


class Port(MikeObject):
    '''
    {
        "uuid": UUID,
        "name": string,
        "number": integer,
        "switch": reference,
    }
    '''
    name = models.CharField(max_length=16, null=False, blank=True)
    number = models.IntegerField(null=True)
    state = models.IntegerField(null=False)

    class Meta:
        unique_together = (('switch', 'number'), ('switch', 'name'))
        abstract = True

    def clean(self):
        if not self.name and not self.number:
            raise ValidationError(_("this taple is not unique"))

    def __unicode__(self):
        return self.uuid
