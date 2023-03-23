from django.shortcuts import render, redirect
from portfolio.models import StudentLeaf, Student, StudentLeafStatus
from edumarket.models import Contract
from tree.models import Leaf
from .data_handle import update_student_leaves

# Create your views here.

def index(request):
    if request.user.is_authenticated:

        sleaves_list = []
        
        for student in Student.objects.all():
            if student.user == request.user:
                our_student = student
        
        update_student_leaves(our_student)

        for sleaf in StudentLeaf.objects.all():
           if sleaf.status.name != 'Not interested':
                if sleaf.student == our_student:
                            sleaves_list.append(sleaf)

        student_courses_list = []

        for contract in Contract.objects.all():
            if contract.student == our_student:
                student_courses_list.append(contract.course)

        return render(request, "portfolio/index.html", {'sleaves_list' : sleaves_list, 'student_courses_list' : student_courses_list })
    
    else:
        return redirect('/accounts')

def student_contracts(request):
    if request.user.is_authenticated:
        our_user = request.user
        contract_list = []
        
        for student in Student.objects.all():
            if student.user == our_user:
                our_student = student
        
        for contract in Contract.objects.all():
            if contract.student == our_student:
                contract_list.append(contract)

        return render(request, "portfolio/contracts.html", {'contract_list' : contract_list}) 
    else:
        return redirect('/accounts')