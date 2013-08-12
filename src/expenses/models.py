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

from django.db import models

class ExpenseCategory(models.Model):

    description = models.CharField(max_length=1000)
    
    class Meta:
        verbose_name_plural = "Expense Categories"
        
class Expense(models.Model):

    description = models.CharField(max_length=1000)
    value = models.DecimalField(max_digits=18, decimal_places=2, default=0)
    date = models.DateTimeField()
    category = models.ForeignKey(ExpenseCategory)
    

