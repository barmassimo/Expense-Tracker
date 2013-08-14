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

class ExpenseManager(models.Manager):
    def get_expense_report(self, expenses):
        report = {}
        
        report['from_date'] = min(e.date for e in expenses)
        report['to_date'] = max(e.date for e in expenses)
        report['days'] = (report['to_date'] - report['from_date']).days
        report['months'] = float(report['days']) / float(30) 
        
        expenses_grouped = []
        for cat in ExpenseCategory.objects.all():
            expenses_grouped.append ({'expenseCategory': cat, 'total': sum([ e.value for e in expenses if e.category == cat])})
        
        report['expenses_grouped'] = expenses_grouped
        
        report['total'] = sum(e.value for e in expenses)
        report['total_per_month'] =  float(report['total']) / report['months'] 
        
        return report

class ExpenseCategory(models.Model):

    description = models.CharField(max_length=1000)
    color = models.CharField(max_length=6, help_text="Example: 0000FF")
    
    def __unicode__(self):
        return self.description
        
    def get_absolute_url(self):
        return reverse('expense_category_detail', kwargs={'pk': self.pk})
        
    class Meta:
        verbose_name_plural = "Expense Categories"
        ordering = ['description']
        
        
class Expense(models.Model):
    description = models.CharField(max_length=1000)
    value = models.DecimalField(max_digits=18, decimal_places=2, default=0)
    date = models.DateField(default=date.today())
    category = models.ForeignKey(ExpenseCategory)
    
    objects = ExpenseManager() 
        
    class Meta:
        ordering = ['-date']
    

