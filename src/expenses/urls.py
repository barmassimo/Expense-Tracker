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

from django.conf.urls import patterns, url

from .views import *

urlpatterns = patterns('',
                       url(r'^index$', IndexView.as_view(), name='index'),

                       url(r'^expense_list$', ExpenseList.as_view(),
                           name='expense_list'),
                       url(r'^expense_list_json$', ExpenseListJson.as_view(),
                           name='expense_list_json'),
                       url(r'^expense_create$', ExpenseCreate.as_view(),
                           name='expense_create'),
                       url(r'^expense_update/(?P<pk>.*)$',
                           ExpenseUpdate.as_view(), name='expense_update'),
                       url(r'^expense_delete/(?P<pk>.*)$',
                           ExpenseDelete.as_view(), name='expense_delete'),

                       url(r'^expense_category_list$', ExpenseCategoryList.as_view(),
                           name='expense_category_list'),
                       url(r'^expense_category_create$', ExpenseCategoryCreate.as_view(),
                           name='expense_category_create'),
                       url(r'^expense_category_update/(?P<pk>\d+)/$',
                           ExpenseCategoryUpdate.as_view(), name='expense_category_update'),
                       url(r'^expense_category_delete/(?P<pk>\d+)/$',
                           ExpenseCategoryDelete.as_view(), name='expense_category_delete'),

                       url(r'^stats$', StatsView.as_view(), name='stats'),
                       )
