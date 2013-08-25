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
from decimal import Decimal
from django.test import TestCase

from .models import Expense, ExpenseCategory

class ExpenseReportTest(TestCase):

    def setUp(self):
        self.cat1 = ExpenseCategory(description = "cat1", color="ff0000")
        self.cat1.save()
        self.cat2 = ExpenseCategory(description = "cat2", color="ff0000")
        self.cat2.save()
        self.cat3 = ExpenseCategory(description = "cat3", color="ff0000")
        self.cat3.save()
        
        self.e1a = Expense(description = "e1a", amount = 10.52, date = date(2013,1,31), category = self.cat1 )
        self.e1a.save()
        self.e1b = Expense(description = "e1b", amount = 1.10, date = date(2013,1,1), category = self.cat1 )
        self.e1b.save()
        self.e2a = Expense(description = "e2a", amount = 1000, date = date(2013,3,31), category = self.cat2 )
        self.e2a.save()
        
    def test_expense_report_dates(self):
        report = Expense.objects.get_expense_report();
        
        self.assertEqual(report['from_date'], date(2013,1,1))
        self.assertEqual(report['to_date'], date(2013,3,31))
        self.assertEqual(report['days'],90)
        self.assertEqual(report['months'], float(90) / float(30))
        
    def test_expense_report_grouping(self):
        report = Expense.objects.get_expense_report();
        
        self.assertEqual(len(report['expenses_grouped']), 2)
        
        for g in report['expenses_grouped']:
            if (g['expenseCategory'] == self.cat1):
                self.assertEqual(g['total'], Decimal('11.62'))
            elif (g['expenseCategory'] == self.cat2):
                self.assertEqual(g['total'], Decimal('1000'))
            else:
                raise Exception("Unknown category")     
       
    def test_expense_report_totals(self):
        report = Expense.objects.get_expense_report();

        self.assertEqual(report['total'], Decimal('1011.62'))        
        self.assertEqual(report['total_per_month'], float(report['total']) / float(report['months']))   
        
        
        
        
        
        
        
        
        
