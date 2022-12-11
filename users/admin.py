from django.contrib import admin

from .models import User, FeedBack, Transaction

admin.site.register(User)
admin.site.register(FeedBack)
admin.site.register(Transaction)
