from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
from account.forms import TransactionForm
from account.models import Check, Transaction

#
# def billing(request):
#     if request.method == 'POST':
#         amount = request.POST["amount"]
#         recipient = request.POST["recipient"]
#         sender = request.POST["sender"]
#         Transaction.objects.create(amount= amount,recipient = recipient,sender= sender)
#         return render(request, 'billing.html', )
#     else:  # GET
#         return render(request, 'billing.html', )


def billing(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            obj = Transaction()  # gets new object
            amount = form.cleaned_data['amount']
            obj.amount = amount
            recipient_id = form.cleaned_data['recipient']
            obj.recipient = recipient_id
            # obj.sender = form.cleaned_data['sender']
            list_sender = form.cleaned_data['sender']
            obj.save()
            count_check = list_sender.count()
            amount_check = amount / count_check
            recipient = Check.objects.get(id = recipient_id)
            for check in list_sender:
                check.balance -= amount_check
                recipient.balance += amount_check
                check.save()

                obj.sender.add(check.id)
            recipient.save()

            return render(request, 'billing.html', )
        return render(request, 'billing.html', )
    else:  # GET
        return render(request, 'billing.html', )

def history(request):
    transactions = Transaction.objects.all()
    return render(request, 'history.html', {'transactions': transactions})


def check(request, id):
    check = Check.objects.get(id= id)
    owner = check.owner
    return render(request, 'details.html',{'check':check,'owner':owner})

def check_list_recipient(request):
    q = request.GET.get('term', '')
    print(q)
    chek_list = list(Check.objects.filter(id = q).exclude(owner=request.user).values('id', 'balance'))
    return JsonResponse({'results': chek_list})

def check_list_sender(request):
    q = request.GET.get('term', '')
    print(q)
    chek_list = list(Check.objects.filter(id = q,owner=request.user).values('id', 'balance'))
    return JsonResponse({'results': chek_list})

def source_history(request):
    chek_list = list()
    for date in Transaction.objects.all().values_list('id','created_at','amount', 'recipient',):
       obj = Transaction.objects.get(id = date[0])
       res = obj.sender.all().values_list('id', flat=True)
       list_date = list(date)
       list_date[1] = date[1].strftime("%H:%M %d.%m.%Y")
       chek_list.append(list_date)
       list_date.append(tuple(res))

    return JsonResponse({'data': chek_list})
