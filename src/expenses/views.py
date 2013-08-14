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

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import View, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse, reverse_lazy

from .models import Expense, ExpenseCategory
from .forms import ExpenseForm
    
class IndexView(TemplateView):
    template_name="expenses/index.html"
    
class ExpenseCategoryList(ListView):
    model = ExpenseCategory
    paginate_by = 10
    
class ExpenseCategoryCreate(CreateView):
    model = ExpenseCategory
    success_url = reverse_lazy('expense_category_list') # default is DetailView
    
class ExpenseCategoryUpdate(UpdateView):
    model = ExpenseCategory
    success_url = reverse_lazy('expense_category_list') # default is DetailView
    
class ExpenseCategoryDelete(DeleteView):
    model = ExpenseCategory
    success_url = reverse_lazy('expense_category_list')
    
class ExpenseList(TemplateView):
    template_name="expenses/expense_list.html"
    
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['form'] = ExpenseForm() 
        context['object_list'] = Expense.objects.all()
        return self.render_to_response(context)
        
    def post(self, request, *args, **kwargs):
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save()
            return HttpResponseRedirect(reverse('expense_list'))

        context = self.get_context_data(**kwargs)
        context['form'] = form
        context['object_list'] = Expense.objects.all()
        return self.render_to_response(context)    
    
class ExpenseCreate(CreateView):
    model = Expense
    template_name="expenses/expense_form_new.html"
    form_class  = ExpenseForm
    success_url = reverse_lazy('expense_list') # default is DetailView
    
class ExpenseUpdate(UpdateView):
    model = Expense
    form_class  = ExpenseForm
    success_url = reverse_lazy('expense_list') # default is DetailView
    
class ExpenseDelete(DeleteView):
    model = Expense
    success_url = reverse_lazy('expense_list')
    
class StatsView(TemplateView):
    template_name="expenses/stats.html"
    
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['report'] = Expense.objects.get_expense_report(Expense.objects.all());
        
        return self.render_to_response(context)    
        
        
        
