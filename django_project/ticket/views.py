import datetime

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.utils import timezone

from users.models import User

from .form import CreateTicketForm, UpdateTicketForm
from .models import Ticket


#view ticket details
@login_required
def ticket_details(request, pk):

        ticket = Ticket.objects.get(pk=pk) # get the ticket with that
        t=User.objects.get(username=ticket.created_by)
        tickets_per_user=t.created_by.all()

        context={'ticket':ticket, 'tickets_per_user':tickets_per_user}
        return render(request,'ticket/ticket_details.html',context)
        # specific ID from the database

'''For Customers'''

def create_ticket(request):
    if request.method =='POST':
        form = CreateTicketForm(request.POST)
        if form.is_valid():
            var= form.save(commit=False)
            var.created_by= request.user
            var.ticket_status= 'Pending'
            var.save()
            messages.info(request,'Your ticket has been successfully submitted. An engineer would be assigned soon.')
            return redirect('dashboard')
        
        else:
            messages.error(request,"something went wrong . please check form input!!")
            return redirect('create-ticket')
    else:
        form = CreateTicketForm()
        context = {'form':form}
        return render(request,'ticket/create_ticket.html',context)
    

#updating a ticket
@login_required
def update_ticket(request,pk):
    ticket = Ticket.objects.get(pk=pk)
    if not ticket.is_resolved:
        if request.method =='POST':
            form = UpdateTicketForm(request.POST , instance=ticket)
            if form.is_valid():
                form.save()
            
                messages.info(request,'Your ticket info has been updated and all the changes are saved in database :)')
                return redirect('dashboard')
        
            else:
                messages.error(request,"something went wrong . please check form input!!1")
        else:
            form = UpdateTicketForm(instance=ticket)
            context = {'form':form}
            return render(request,'ticket/update_ticket.html',context)
    else:
        messages.error(request, 'you cannot make any changes!!')
        return redirect('dashboard')
#viewing all created tickets'
@login_required
def all_tickets(request):
        tickets=Ticket.objects.filter(created_by=request.user).order_by('-date_created')
        context={'tickets': tickets}
        return render(request, 'ticket/all_tickets.html', context)

"""For Engineer"""

#view ticket queue
@login_required
def ticket_queue(request):
    tickets= Ticket.objects.filter(ticket_status='Pending')
    context= {'tickets':tickets}
    return render(request,'ticket/ticket_queue.html',context)

# accept a ticket from the queue
@login_required
def accept_ticket(request, pk):
    tickets=Ticket.objects.get(pk=pk)
    tickets.assigned_to=request.user
    tickets.ticket_status=" Active"
    tickets.accepted_date= timezone.now()
    tickets.save()
    messages.info(request,'Ticket has been accepted. please resolve as soon as possible!')
    return redirect('workspace')

@login_required
def close_ticket(request, pk):
    
    ticket=Ticket.objects.get(pk=pk)
    
    ticket.ticket_status=" Completed"
    ticket.is_resolved=True
    ticket.closed_date= datetime.datetime.now()
    ticket.save()
    messages.info(request,'Ticket has been resolved. Thank you brilliant support engineer')
    return redirect('ticket-queue')


#tickets engineer is workin on
@login_required
def workspace(request):
    tickets=Ticket.objects.filter(assigned_to=request.user, is_resolved=False )
    context= {
            'tickets':tickets,
            }
    return render(request,"ticket/workspace.html", context)


#all close/resolved tickets
@login_required
def all_closed_tickets(request):
    tickets=Ticket.objects.filter(assigned_to=request.user, is_resolved=True)
    context={'tickets':tickets}
    return render(request, "ticket/all_closed_tickets.html", context)



def confirm_resolution(request, pk):
    ticket=Ticket.objects.get(pk=pk)
    # logic to confirm resolution
    if ticket.ticket_status != 'Completed':
        # Update the ticket status to 'Completed'
        ticket.ticket_status = 'Completed'
        ticket.save()
    return render(request, 'ticket/confirmation.html', {'ticket': ticket})


