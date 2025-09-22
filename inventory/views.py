from django.shortcuts import render, redirect,get_object_or_404
from inventory.models import Purchase
from decimal import Decimal
import datetime

def purch(request):
    error = None
    
    if request.method == "POST":
        invoice = request.POST.get("purchaseinvoiceno")
        supplier = request.POST.get("suppliername")
        date_str = request.POST.get("purchasedate")
        amount_str = request.POST.get("purchaseamount")
        
       
        if not invoice or not supplier or not date_str or not amount_str:
            error = "All fields are required."
        
        
        elif Purchase.objects.filter(invoice=invoice).exists():
            error = f"Invoice '{invoice}' already exists!"
        
       
        else:
            try:
                date = datetime.datetime.strptime(date_str, "%d/%m/%Y").date()
            except ValueError:
                error = "Date must be in DD/MM/YYYY format."
        
        
        if not error:
            try:
                amount = Decimal(amount_str)
            except:
                error = "Amount must be numeric."
        
       
        if not error:
            Purchase.objects.create(
                invoice=invoice,
                supplier=supplier,
                date=date,
                amount=amount
            )
            return redirect('/purchaselist') 
    
    
    queryset = Purchase.objects.all()
    context = {"purch": queryset,"error": error}
    return render(request, "purchaselist.html", context)

def purchase_delete(request, id):
    obj = get_object_or_404(Purchase, id=id)
    obj.delete()
    return redirect('/purchaselist')

def purchase_update(request, id):
    purchase = get_object_or_404(Purchase, id=id)
    
    if request.method == "POST":
        purchase.invoice= request.POST.get('purchaseinvoiceno')
        purchase.supplier = request.POST.get('suppliername')
        
       
        from datetime import datetime
        date_str = request.POST.get('purchasedate')
        purchase.date = datetime.strptime(date_str, '%d/%m/%Y').date()
        
        purchase.amount = request.POST.get('purchaseamount')
        purchase.save()
        return redirect('/purchaselist')  
    
    return render(request, 'updatepurchase.html', {'purchase': purchase})