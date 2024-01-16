from django.shortcuts import render,redirect,  get_object_or_404
from .models import Train, Seat,Review
from django.views.generic import DetailView
from .forms import ReviewForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

@method_decorator(login_required, name='dispatch')
class buy_ticket(DetailView):
    model = Train
    pk_url_kwarg = 'id' #train id eta
    template_name = 'buy_ticket.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        train_id = self.kwargs.get('id')
        train = get_object_or_404(Train, pk=train_id)
        seats = Seat.objects.filter(train=train)
        context['train'] = train
        context['seats'] = seats

        trainnn = Review.objects.filter(train=train)
       
        comments = train.review.all()
        comment_form = ReviewForm()
        context['comments'] = comments
        context['comment_form'] = comment_form

        return context
    
    def post(self, request, *args, **kwargs):
        comment_form = ReviewForm(data=self.request.POST)
        train = self.get_object() 
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.train = train  
            new_comment.save()
        return self.get(request, *args, **kwargs)
    
@login_required
def buy(request, tid, sid):
    train = Train.objects.get(pk=tid)
    price = train.price
    account = request.user.account
    initial_balance = account.balance

    if initial_balance >= price:  
        new_balance = initial_balance - price # buy korar por balance
        account.balance = new_balance
        account.save(update_fields=['balance'])

        # seat = Seat.objects.get(pk=sid, train=train)
        seat = get_object_or_404(Seat, pk=sid, train=train, active=False)
        print(f"seat e click korechi: {seat}")
        print(f"train ta holo: {train}")
        seat.active = True
        seat.save(update_fields=['active'])

        return redirect("buy_ticket", id=tid)
    else:
        return redirect("buy_ticket", id=tid)


        