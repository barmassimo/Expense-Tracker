# ExpenseTracker - a simple, Django based expense tracker.
# Copyright (C) 2013 Massimo Barbieri - http://www.massimobarbieri.it
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView
from django.contrib import admin

import os

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^expenses/', include('expenses.urls')),
                       url(r'^favicon\.ico$', RedirectView.as_view(url='/static/expenses/img/favicon.ico')),
                       url(r'^$', RedirectView.as_view(url= '/expenses/index')),
                       )

# Disable admin on Google App Engine
if not os.getenv('SERVER_SOFTWARE', '').startswith('Google App Engine'):
    urlpatterns.append(url(r'^admin/', include(admin.site.urls)))