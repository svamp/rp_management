from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from userena.models import UserenaBaseProfile

class Profile(UserenaBaseProfile):
	user = models.OneToOneField(User,
								unique=True,
								verbose_name=_('user'),
								related_name='profile')
	class Meta(object):
		verbose_name=_('profile')
		verbose_name_plural=_('profiles')


