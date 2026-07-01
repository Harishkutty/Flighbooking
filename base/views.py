from django.shortcuts import render, redirect
from .models import FlightModel, BookingModel, ConfirmModel

# Create your views here.


def home(request):
    data = FlightModel.objects.all()
    
    from_city = request.GET.get('from_city')
    to_city = request.GET.get('to_city')
    
    if from_city:
        data = FlightModel.objects.filter(from_city__icontains = from_city)
        
    if to_city:
        data = FlightModel.objects.filter(to_city__icontains = to_city)
    
    return render(request, 'home.html', {'data': data})


def booking(request):
    bookings = BookingModel.objects.all()
    return render(request, 'booking.html', {'data': bookings})


def history(request):
    data = ConfirmModel.objects.all()
    return render(request, 'history.html', {'data': data})


def profile(request):
    return render(request, 'profile.html')


def logout(request):
    return render(request, 'logout.html')


def support(request):
    return render(request, 'support.html')


def about(request):
    return render(request, 'about.html')


def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')


def book(request, id):

    data = FlightModel.objects.get(id=id)

    if request.method == "POST":

        booking = BookingModel.objects.create(

            flight_company=data.flight_company,
            flight_name=data.flight_name,
            flight_no=data.flight_no,
            from_city=data.from_city,
            to_city=data.to_city,
            depature_time=data.depature_time,
            depature_date=data.depature_date,
            price=data.price,

            passenger_name=request.POST.get('name'),
            email=request.POST.get('email'),
            phone_no=request.POST.get('phnumber'),
            adhar_no=request.POST.get('adharnum'),
            age=request.POST.get('age'),
            seat_class=request.POST.get('class'),
            seat_no=request.POST.get('snumber')

        )

        # return render(request, 'booking.html', {'data': booking})
        return redirect('booking')

    return render(request, 'book.html', {'data': data})


def remove(request,pk):
    data = BookingModel.objects.get(id=pk)
    ConfirmModel.objects.create(
        flight_company=data.flight_company,
        flight_name=data.flight_name,
        flight_no=data.flight_no,
        from_city=data.from_city,
        to_city=data.to_city,
        depature_time=data.depature_time,
        depature_date=data.depature_date,
        price=data.price,
            
        passenger_name = data.passenger_name,
        email = data.email,
        phone_no = data.phone_no,
        adhar_no = data.adhar_no,
        age = data.age,
        seat_class = data.seat_class,
        seat_no = data.seat_no
            
    )
    data.delete()
    return redirect('history')
    # return render(request, 'trash.html')
    
def hremove(request,pk):
   data = ConfirmModel.objects.get(id=pk)
   data.delete()
   return redirect('history')
        
