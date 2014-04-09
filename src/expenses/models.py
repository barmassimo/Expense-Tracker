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

from datetime import date
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models import Min, Max, Sum, Count


class ExpenseManager(models.Manager):

    def get_expense_report(self):

        aggregate_data = Expense.objects.aggregate(
            Min('date'), Max('date'), Count('pk'), Sum('amount'))

        if (aggregate_data['pk__count'] == 0):
            return {'total': 0, 'total_per_month': 0}

        report = {}

        report['from_date'] = aggregate_data['date__min']
        report['to_date'] = aggregate_data['date__max']
        report['days'] = (report['to_date'] - report['from_date']).days + 1
        report['months'] = float(report['days']) / float(30)
        report['total'] = aggregate_data['amount__sum']
        report['total_per_month'] = float(report['total']) / report['months']

        categories = dict((x.pk, x) for x in ExpenseCategory.objects.all())

        category_data = Expense.objects.values('category').annotate(
            total=Sum('amount')).order_by('category')
        category_data = sorted(
            category_data, key=lambda x: int(-1 * x['total']))

        expenses_grouped = []
        for c in category_data:
            expenses_grouped.append(
                {'expenseCategory': categories[c['category']], 'total': c['total']})

        report['expenses_grouped'] = expenses_grouped

        return report


class ExpenseCategory(models.Model):

    description = models.CharField(max_length=1000, unique=True)
    color = models.CharField(max_length=6, help_text="Example: 0000FF")

    def __str__(self):
        return self.description

    def get_absolute_url(self):
        return reverse('expense_category_detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name_plural = "Expense Categories"
        ordering = ['description']


class Expense(models.Model):
    description = models.CharField(max_length=1000)
    amount = models.DecimalField(max_digits=18, decimal_places=2, default=0)
    date = models.DateField(default=date.today())
    category = models.ForeignKey(ExpenseCategory)

    def __str__(self):
        return self.description

    objects = ExpenseManager()

    class Meta:
        ordering = ['-date', '-pk']
