from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.template.loader import render_to_string

from .models import Rule
from .forms import RuleForm

def rule_list(request):
    rules = Rule.objects.all()
    return render(request, 'rules/rule_list.html', {'rules': rules})


def save_rule_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            rules = Rule.objects.all()
            data['html_rule_list'] = render_to_string('rules/includes/partial_rule_list.html', {
                'rules': rules
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

def rule_create(request):
    if request.method == 'POST':
        form = RuleForm(request.POST)
    else:
        form = RuleForm()
    print("OK")
    return save_rule_form(request, form, 'rules/includes/partial_rule_create.html')


def rule_update(request, pk):
    rule = get_object_or_404(Rule, pk=pk)
    if request.method == 'POST':
        form = RuleForm(request.POST, instance=rule)
    else:
        form = RuleForm(instance=rule)
    return save_rule_form(request, form, 'rules/includes/partial_rule_update.html')



def rule_delete(request, pk):
    rule = get_object_or_404(Rule, pk=pk)
    data = dict()
    if request.method == 'POST':
        rule.delete()
        data['form_is_valid'] = True
        rules = Rule.objects.all()
        data['html_rule_list'] = render_to_string('rules/includes/partial_rules_list.html', {
            'rules': rules
        })
    else:
        context = {'rule': rule}
        data['html_form'] = render_to_string('rules/includes/partial_rule_delete.html', context, request=request)
    return JsonResponse(data)
