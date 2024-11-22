from django.contrib.auth import authenticate, login
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
from datetime import datetime
from django.core.paginator import Paginator
from django.http import JsonResponse
import openpyxl
from openpyxl import load_workbook
from openpyxl import Workbook
from .forms import * #
import logging

logger = logging.getLogger(__name__)



def LoginView(request):
    if request.user.is_authenticated:
        return redirect('staff')
    
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')
        
        if not username or not password:
            messages.error(request, 'Please fill in both email and password.')
            return render(request, 'theme/login.html')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome Back, {user.first_name}')
            request.session['notification_displayed'] = True  # Mark notification as shown
            next_url = request.GET.get('next', 'staff')
            return redirect(next_url)
        else:
            logger.warning(f"Failed login attempt for email: {username} at {now()}")
            messages.error(request, 'Invalid login credentials.')
            return render(request, 'theme/login.html')
    else:
        return render(request, 'theme/login.html')

def Dashboard(request):
    return render(request, 'theme/admin_2.html')

def AllClients(request):
    clients = User.objects.filter(user_type='Customer').select_related('client_profile')
    client_count = User.objects.count()
    paginator = Paginator(clients, 10)  # Show 10 clients per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'theme/clients.html',{'clients':clients, 'page_obj':page_obj})


def ClientDetails(request, client_id):

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
    return render(request, 'theme/client_details.html', {'client': client, 'is_verified': is_verified, 'credit_score': credit_score, 'client_profile': client_profile})

#Verifying the client
def verify_user(request, client_id):
    user = get_object_or_404(User, pk=client_id, user_type='Customer')

    # Update the is_verified field directly in the User model
    user.is_verified = True
    user.save()

    return redirect('client_details', client_id=client_id)


def verify_user(request, client_id):
    user = get_object_or_404(User, pk=client_id, user_type='Customer')

    # Update the is_verified field directly in the User model
    user.is_verified = True
    user.save()

    return redirect('client_details', client_id=client_id)



def CreateClientView(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        r_address = request.POST.get('r_address')
        id_number = request.POST.get('nrc')
        gender = request.POST.get('sex')
        phone = request.POST.get('phone_number')
        empolyee_number = request.POST.get('employee_number')
        bank = request.POST.get('bank')
        bank_acc = request.POST.get('bank_acc')
        profile_pic = request.POST.get('profile_pic')
        id_front = request.POST.get('id_front')
        id_back = request.POST.get('id_back')
        dob = request.POST.get('dob')

        try:
            # Parse the date string
            formatted_date = datetime.strptime(dob, '%Y-%m-%d').date()
        except ValueError:
            messages.error(request, 'Invalid date format.')
            return render(request, 'theme/create_client.html', {
                'email': email, 'first_name': first_name, 'last_name': last_name, 
                'r_address': r_address, 'id_number': id_number, 'gender': gender,
                'phone': phone, 'empolyee_number': empolyee_number, 'bank': bank, 
                'bank_acc': bank_acc, 'dob': dob
            })

        # Check if the user already exists by email
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists.')
            return render(request, 'theme/create_client.html', {
                'email': email, 'first_name': first_name, 'last_name': last_name, 
                'r_address': r_address, 'id_number': id_number, 'gender': gender,
                'phone': phone, 'empolyee_number': empolyee_number, 'bank': bank, 
                'bank_acc': bank_acc, 'dob': dob
            })
        
        # Check if client with this NRC number exists
        elif User.objects.filter(id_number=id_number).exists():
            messages.error(request, 'Client with this NRC Number already exists.')
            return render(request, 'theme/create_client.html', {
                'email': email, 'first_name': first_name, 'last_name': last_name, 
                'r_address': r_address, 'id_number': id_number, 'gender': gender,
                'phone': phone, 'empolyee_number': empolyee_number, 'bank': bank, 
                'bank_acc': bank_acc, 'dob': dob
            })

        # Create the user
        user = User.objects.create(
            profile_pic=profile_pic,
            email=email,
            first_name=first_name,
            last_name=last_name,
            address=r_address,
            id_number=id_number,
            dob=formatted_date,
            gender=gender,
            id_front=id_front,
            id_back=id_back,
            user_type='Customer'
        )

        # # Check if ClientProfile already exists for this user
        if ClientProfile.objects.filter(user=user).exists():
            messages.error(request, 'Client profile already exists for this user.')
            return render(request, 'theme/create_client.html', {
                'email': email, 'first_name': first_name, 'last_name': last_name, 
                'r_address': r_address, 'id_number': id_number, 'gender': gender,
                'phone': phone, 'empolyee_number': empolyee_number, 'bank': bank, 
                'bank_acc': bank_acc, 'dob': dob
            })

        # Create the client profile
        ClientProfile.objects.create(
            user=user,
            empolyee_number=empolyee_number,
            bank=bank,
            bank_acc=bank_acc,
            pin='1111'  
        )

        # Display success message
        messages.success(request, 'Client successfully created.')
        return redirect('theme/clients.html')
    
    return render(request, 'theme/clients.html')
def Loans(request):
    loans = Loan.objects.all().select_related('customer__user')
    combined_data = []

    for loan in loans:
        client_profile = loan.customer.user.client_profile
        combined_data.append((loan, client_profile))

    return render(request, 'theme/loans.html', {'combined_data': combined_data})



def Reports(request):
    return render(request, 'theme/reports.html')

def ClosedLoans(request):
    return render(request, 'theme/closed_loans.html')


def ActiveLoans(request):
    return render(request, 'theme/active_loans.html')


def PendingLoansView(request):
    pending_loans = Loan.objects.filter(status='pending')
    combined_data = []

    for loan in pending_loans:
        # Access the client profile directly through the loan's customer
        client = loan.customer 
        combined_data.append((loan, client))

    return render(request, 'theme/pending_loans.html', {'combined_data': combined_data})


def CreatClient(request):
    return render(request, 'theme/create_client.html')



def AttachClient(request):
    clients = User.objects.filter(user_type='Customer').select_related('client_profile')
    client_count = User.objects.count()
    paginator = Paginator(clients, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    client_id = request.GET.get('client_id')
    if client_id:
        client = get_object_or_404(User, id=client_id)
        return JsonResponse({
            'client': {
                'first_name': client.first_name,
                'last_name': client.last_name,
                'nrc_number': client.client_profile.nrc_number,
                'email': client.email,
            }
        })

    return render(request, 'theme/attach_client.html', {
        'clients': clients,
        'page_obj': page_obj,
    })


def ClientAttachement(request, client_id):
    try:
        client = User.objects.get(id=client_id)
        data = {
            'first_name': client.first_name,
            'last_name': client.last_name,
            'email': client.email,
            'id_number': client.id_number,
            'client_id': client.id
            
        }
        return JsonResponse(data, status=200)
    except client.DoesNotExist:
        return JsonResponse({'error': 'Client not found'}, status=404)
   

def CreateLoan(request):
    return render(request, 'theme/create_loan.html')


def passIDToAddLoan(request, client_id):
    client = User.objects.get(id=client_id)
    loanProducts = LoanProduct.objects.all()
  
    return render(request, 'theme/create_loan.html', {'client': client, 'loanProducts': loanProducts})


def ListLoanProducts(request):
    products = LoanProduct.objects.all()
    return render(request, 'theme/loan_products.html', {'products': products})


def Profile(request):
    return render(request, 'theme/profile.html')


def calculateLoanRepayment(request):
    loan_product_id = request.POST.get('loan-product-id')
    principle = request.POST.get('principle')

    try:
        loan_product = LoanProduct.objects.get(id=loan_product_id)

        if loan_product.interest_rate_method == 'Flate Rate':
            try:
                total_repayment = FlatRateProducts.objects.get(id=loan_product_id).calaculateTotalPayment(principle)
            except ObjectDoesNotExist:
                return HttpResponseNotFound("Flat Rate product not found.")

        elif loan_product.interest_rate_method == 'Reducing Balance':
            try:
                total_repayment = ReducingBalance.objects.get(id=loan_product_id).calculateTotalPayment(principle)
            except ObjectDoesNotExist:
                return HttpResponseNotFound("Reducing Balance product not found.")

        elif loan_product.interest_rate_method == 'Interest Only':
            try:
                total_repayment = InterestOnly.objects.get(id=loan_product_id).calculateToatalPayment(principle)
            except ObjectDoesNotExist:
                return HttpResponseNotFound("Interest Only product not found.")

        return JsonResponse({'total_repayment': total_repayment})

    except LoanProduct.DoesNotExist:
        return HttpResponseNotFound("The specified loan product does not exist.")
    except ValidationError as e:
        return JsonResponse({'error': str(e)}, status=400)

def CreateExcelTemplate(request):
    # Correctly instantiate the Workbook
    wb = Workbook()

    # Access the active worksheet
    ws = wb.active

    # Set the title of the worksheet
    ws.title = 'Bulk Clients'

    # Add header row
    ws.append(['First Name', 'Last Name', 'Residential Address', 'NRC Number', 'Sex', 'Email', 'Phone Number', 'Employee Number', 'Bank', 
               'Bank Account', 'City/Town/Province', 'Date of Birth'])

    # Prepare the HTTP response to serve the file
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="Bulk_Clients_Template.xlsx"'

    # Save the workbook to the response
    wb.save(response)

    return response



def UploadBulkClientTemplate(request):
    if request.method == 'POST':
        form = BulkClientUploadForm(request.POST, request.FILES)
        if form.is_valid():
            excel_file = request.FILES['file']
            wb = load_workbook(excel_file)
            sheet = wb.active

            for row in sheet.iter_rows(min_row=2, values_only=True):
                first_name, last_name, r_address, id_number, gender, email, phone_number, employee_number, bank, bank_acc, city, dob = row

                # Process the date correctly based on its type
                if isinstance(dob, datetime):  # Check if dob is a datetime object
                    formatted_date = dob.date()  # Convert to date
                elif isinstance(dob, str):  # If it's a string, try to parse it
                    try:
                        formatted_date = datetime.strptime(dob, '%Y-%m-%d').date()
                    except ValueError:
                        messages.error(request, f'Invalid date format for {first_name} {last_name} in the uploaded template.')
                        return redirect('clients')  # Redirect after error
                else:
                    formatted_date = None  # Handle None or unexpected type

                # Check if the user already exists by email
                existing_user = User.objects.filter(email=email).first()

                if existing_user:
                    messages.warning(request, f'Email already exists for {first_name} {last_name}. Skipping entry.')

                    # Check if ClientProfile already exists for this user
                    existing_profile = ClientProfile.objects.filter(user=existing_user).first()
                    if existing_profile:
                        messages.warning(request, f'ClientProfile already exists for {first_name} {last_name}. Skipping entry.')
                        continue
                else:
                    # Create new user/client
                    existing_user = User.objects.create(
                        first_name=first_name,
                        last_name=last_name,
                        email=email,
                        phone_number=phone_number,
                        gender=gender,
                        id_number=id_number,
                        location=r_address,  # Assuming you want to store this in location
                        city=city,
                        dob=formatted_date  # Use 'dob' from User model
                    )

                # Check if ClientProfile already exists for the user before creating
                if not ClientProfile.objects.filter(user=existing_user).exists():
                    # Create the corresponding ClientProfile
                    ClientProfile.objects.create(
                        user=existing_user,
                        empolyee_number=employee_number,  # Check for typo and correct if needed
                        bank=bank,
                        bank_acc=bank_acc,
                        balance=0.00  # or set a default balance if applicable
                    )
                    messages.success(request, f'{first_name} {last_name} added successfully.')
                else:
                    messages.warning(request, f'ClientProfile already exists for {first_name} {last_name}. Skipping profile creation.')

            return redirect('clients')  
    else:
        form = BulkClientUploadForm()

    return render(request, 'theme/clients.html', {'form': form})



def BulkClientUploadView(request):
    return render(request,'theme/upload_bulk_client_template.html')



#Create Loan Product
def CreateLoanProduct(request):
    products = LoanProduct.objects.all()
    if not products:
        print("No loan products available.")
    return render(request, 'theme/loan_products.html', {'products': products})



# Post new loan product
def NewLoanProduct(request):
    if request.method == 'POST':
        product_name = request.POST['product-name']
        description = request.POST['desc']
        interest_rate = request.POST['interest-rate']
        interest_rate_method = request.POST['interest-rate-method']
        duration_period = request.POST['duration-period']
        minimum_amount = request.POST['min-amount']
        maximum_amount = request.POST['max-amount']
        
        newLoanProduct = LoanProduct(
            product_name = product_name,
            description = description,
            interest_rate = interest_rate,
            interest_rate_method = interest_rate_method,
            duration_period = duration_period,
            minimum_amount = minimum_amount,
            maximum_amount = maximum_amount

        ) 

        newLoanProduct.save()

        if newLoanProduct:
            messages.success(request, 'Loan product created successfully.')
        else:
            messages.error(request, 'Loan product creation failed.')
    

    return render(request, 'theme/create_loan_product.html')
