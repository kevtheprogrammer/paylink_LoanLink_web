from django.shortcuts import render
from account.models import *
from loan.models import *
from account.models import *
from payment.models import *
from rest_framework import viewsets, status
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import redirect, get_object_or_404
from django.db.models import Sum
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

def LoginView(request):
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page
            messages.success(request, 'Welcome Back ' + user.first_name)
            return redirect('admin-dashboard')
        else:
            messages.error(request, 'Wrong email or password.')
            return render(request, 'core/login.html')  
           
    else:
        return render(request, 'core/login.html')  
    
@login_required
def AdminDasboard(request):
    clients = User.objects.filter(user_type='Customer').select_related('client_profile')
    total_amount = Loan.objects.filter(status='active').aggregate(total_amount=Sum('amount'))['total_amount']
    payable_amount = Loan.objects.filter(status='active').aggregate(payable_amount=Sum('payable_amount'))['payable_amount']
    total_interest = Loan.objects.filter(status='active').aggregate(total_interest=Sum('total_interest'))['total_interest']
    total_amount = Loan.objects.filter(status='active').aggregate(total_amount=Sum('amount'))['total_amount']
    loan_applications = Loan.objects.filter(status='pending').count()
    active_loan_count = Loan.objects.filter(status='active').count()
    closed_loan_count = Loan.objects.filter(status='closed').count()
    customer_count = User.objects.filter(user_type='Customer').count()
    user = User.objects.all()
    logged_user = request.user 
    

    return render(request, 'core/admin_dashboard.html', {'clients': clients, 'user': user, 'total_amount': total_amount, 'total_interest': total_interest, 'loan_applications': loan_applications,
                                                         'payable_amount': payable_amount, 'active_loan_count': active_loan_count, 'customer_count': customer_count, 'closed_loan_count': closed_loan_count, 'logged_user': logged_user })


    
def ClientListView(request):
    clients = User.objects.filter(user_type='Customer').select_related('client_profile')
    client_count = User.objects.count()
    return render(request, 'core/clients.html', {'clients': clients})


def ActiveClientListView(request):
    active_loans = Loan.objects.filter(status='active').select_related('customer__user')
    combined_data = []

    for loan in active_loans:
        client_profile = loan.customer.user.client_profile
        combined_data.append((loan, client_profile))

    return render(request, 'core/active_loans.html', {'combined_data': combined_data})

def PendingLoansView(request):
    pending_loans = Loan.objects.filter(status='pending')
    combined_data = []

    for loan in pending_loans:
        # Access the client profile directly through the loan's customer
        client = loan.customer 
        combined_data.append((loan, client))

    return render(request, 'core/pending_loans.html', {'combined_data': combined_data})


def ClosedLoansView(request):
    clients = User.objects.filter(user_type='Customer').select_related('client_profile')
    active_loans = Loan.objects.filter(status='closed')
    combined_data = []
    for loan in active_loans:
        client = clients.filter(client_profile__user_id=loan.customer_id).first()
        combined_data.append((loan, client))
    return render(request, 'core/closed_loans.html', {'combined_data': combined_data})



def RejectedLoansView(request):
    clients = User.objects.filter(user_type='Customer').select_related('client_profile')
    rejected_loans = Loan.objects.filter(status='rejected')
    combined_data = []

    for loan in rejected_loans:
        # Access the client profile directly through the loan's customer
        client = loan.customer 
        combined_data.append((loan, client))
    return render(request, 'core/rejected_loans.html', {'combined_data': combined_data})

# def ClientDetailsView(request, client_id):
#     clients = User.objects.filter(user_type='Customer', pk=client_id).select_related('client_profile')
#     is_verified = clients.client_profile.is_verified if hasattr(clients, 'client_profile') else False
#     return render(request, 'core/client_datails.html', {'clients': clients, 'is_verified': is_verified})


def ClientDetailsView(request, client_id):
    # Retrieve the user object or return a 404 error if not found
    client = get_object_or_404(User.objects.select_related('client_profile'), user_type='Customer', pk=client_id)
    
    # Access the related ClientProfile
    client_profile = client.client_profile
    
    # Fetch the credit score related to the client
    credit_score = None
    if hasattr(client_profile, 'creditscore'):
        credit_score = client_profile.CreditScore.credit_score
        
    
    # Access is_verified status directly from the User model
    is_verified = client.is_verified
    print(is_verified)
    print(credit_score)
    
    return render(request, 'core/client_datails.html',  {'client': client, 'is_verified': is_verified, 'credit_score': credit_score})



def LoanDetailsView(request, client_id):

    # Retrieve the client profile using the client_id
    client_profile = get_object_or_404(ClientProfile, user_id=client_id)

    # Retrieve the loan associated with the client
    loan = Loan.objects.filter(customer=client_profile).first()

    # Retrieve the credit score associated with the client
    credit_score = CreditScore.objects.filter(client=client_profile).first()

    # Render the template with loan details and credit score
    return render(request, 'core/loan_details.html', {'loan': loan, 'credit_score': credit_score, 'client_profile': client_profile})


def SearchClient(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        
        # Validate the query
        if not query:
            return render(request, 'core/search_client.html', {'error': 'Please provide a search query.'})
        
        # Search for the client
        clients = User.objects.filter(user_type='Customer').filter(id_number=query) | User.objects.filter(user_type='Customer', phone_number=query)
        
        if not clients:
            return render(request, 'core/search_client.html', {'error': 'No client found with the given ID or phone number.'})
        print(clients)
        
        return render(request, 'core/search_client.html', {'clients': clients})
    else:
        raise Http404("Only GET method is allowed for this view.")
  
    
def verify_user(request, client_id):
    user = get_object_or_404(User, pk=client_id, user_type='Customer')

    # Update the is_verified field directly in the User model
    user.is_verified = True
    user.save()

    return redirect('client_details', client_id=client_id)

def ApproveLoan(request, client_id):
    try:
        # Assuming you want to approve the loan for a specific client
        # You may need to adjust this query based on your actual logic
        loans = Loan.objects.filter(customer__user__id=client_id, status='pending')
        
        # Assuming you only want to approve the first pending loan found
        if loans.exists():
            loan = loans.first()
            loan.status = 'active'
            loan.save()

            # generate transaction 
            loan_transaction = LoanTransaction(
                loan_obj=loan,
                amount=loan.amount,  # Provide the amount
                is_payment_made=True,  # Set the payment status
                status='pending',  # Set the status
                transaction_type='Disbursement',  # Set the transaction type
                client=loan.customer,
                # approved_at=datetime.datetime.now(),  # Set the approval date/time
            )
            loan_transaction.save()
            # Redirect to some page after approval
            messages.success(request, 'Loan activated successfully!')
        else:
            # Handle case where no pending loan is found for the client
             messages.error(request, 'No pending loan found for this client.')
    except Loan.DoesNotExist:
        # Handle case where loan doesn't exist
        messages.error(request, 'Loan not found.')

    return redirect('pending_loans')



def RejectLoan(request, client_id):
    try:
        # Assuming you want to approve the loan for a specific client
        # You may need to adjust this query based on your actual logic
        loans = Loan.objects.filter(customer__user__id=client_id, status='pending')
        
        # Assuming you only want to approve the first pending loan found
        if loans.exists():
            loan = loans.first()
            loan.status = 'rejected'
            loan.save()
            # Redirect to some page after approval
            messages.success(request, 'Loan rejected successfully!')
        else:
            # Handle case where no pending loan is found for the client
             messages.error(request, 'No pending loan found for this client.')
    except Loan.DoesNotExist:
        # Handle case where loan doesn't exist
        messages.error(request, 'Loan not found.')

    return redirect('pending_loans')



def TransactionsView(request):
    transactions = LoanTransaction.objects.all()
    return render(request, 'core/transactions.html', {'transactions': transactions})


def Notifications(request):
    notifications = Notification.objects.all()
    return render(request, 'core/notifications.html', {'notifications': notifications})
