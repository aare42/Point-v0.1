from django.shortcuts import get_object_or_404, render, redirect
from datetime import datetime
# Create your views here.

from django.http import HttpResponse
from .models import Course, Contract, ContractStatusChange, ContractStatus
from portfolio.models import Student
from tree.models import Leaf


def index(request):
    course_list = Course.objects.order_by('name')
    context = {
        'course_list': course_list,
    }
    return render(request, 'edumarket/index.html', context)


def course_detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    leaves_inside = Leaf.objects.filter(course=course)
    try:
        request_student = Student.objects.get(user = request.user)
        try:
            contract = Contract.objects.get(course=course, student=request_student)
        except Contract.DoesNotExist:
            if request.method == 'POST':
                form = ContractForm(request.POST)
                if form.is_valid():
                    contract = form.save(commit=False)
                    contract.user = request.user
                    contract.course = course
                    contract.save()

                    contract_status_change = ContractStatusChange(contract = contract, new_status = ContractStatus.objects.get(name='requested'), date = datetime.now(), initiator = request.user)
                    contract_status_change.save()

                    return redirect('edumarket/course_detail.html', course_id=course_id)
            else:
                form = ContractForm()
            return render(request, 'edumarket/course_detail.html', {'course': course, 'form': form, 'leaves_inside': leaves_inside})
        else:
            return render(request, 'edumarket/course_detail.html', {'course': course, 'contract': contract, 'leaves_inside': leaves_inside})
    except Student.DoesNotExist:
        return redirect('/accounts')
        