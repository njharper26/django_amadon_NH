from django.shortcuts import render, redirect

def index(request):

    directory = {
        'item1' : 'Bat',
        'item2' : 'Cap',
        'item3' : 'Ball',
        'item4' : 'Glove',
        'item5' : 'Cleat',
        'item1_price' : '100',
        'item2_price' : '20',
        'item3_price' : '10',
        'item4_price' : '150',
        'item5_price' : '75',
        'item1_id' : 'p1',
        'item2_id' : 'p2',
        'item3_id' : 'p3',
        'item4_id' : 'p4',
        'item5_id' : 'p5'
    }

    return render(request, 'ama/index.html', directory)

def process(request):

    directory = {
        'item1' : 'bat',
        'item2' : 'cap',
        'item3' : 'ball',
        'item4' : 'glove',
        'item5' : 'cleats',
        'p1' : '100',
        'p2' : '20',
        'p3' : '10',
        'p4' : '150',
        'p5' : '75',
    }

    if request.method == 'POST':

        i_id = request.POST['item_id']
        i_type = request.POST['item_type']
        i_quant = request.POST['item_quant']
        i_total = int(directory[i_id]) * int(i_quant)
        
        order = {
            'type' : i_type,
            'quant' : i_quant,
            'total' : i_total
        }

        run_total = {
            'quant' : i_quant,
            'total' : i_total
        }

        request.session['order'] = []
        request.session['order'].append(order)

        if not 'run_quant' in request.session:
            request.session['run_quant'] = 0
        
        request.session['run_quant'] += int(run_total['quant'])
        
        if not 'run_cost' in request.session:
            request.session['run_cost'] = 0
        
        request.session['run_cost'] += int(run_total['total'])

        return redirect('/amadon/checkout')

    else:
        return redirect('/amadon')

def checkout(request):

    order = {
        'type' : request.session['order'][0]['type'],
        'quant' : request.session['order'][0]['quant'],
        'total' : request.session['order'][0]['total'],
        'run_quant' : request.session['run_quant'],
        'run_cost' : request.session['run_cost']
    }
    print order

    return render(request, 'ama/checkout.html', order)