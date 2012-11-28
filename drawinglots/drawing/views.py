from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.core.cache import cache

from models import Game, Item
from forms import ItemForm

import logging
import json

def guest_key(item_id):

    return 'item:%s' % (item_id)

def winner_key(item_id):

    return 'drawing:%s' % (item_id)

def get_n_guests(item_id):
    n_guests = redis.get(guest_key(item_id))
    if n_guests is None:
        n_guests = 0

    return int(n_guests)


@login_required
def host(request):
    if request.method=='POST':
        game = Game.objects.create(owner=request.user)

        return HttpResponseRedirect(reverse_lazy('drawing_demo', kwargs={
                                    'game_id': game.pk,
                                    }))

    games = Game.objects.filter(owner=request.user).order_by('-created_time')

    return render(request, 'drawing/host.html', {
                  'games': games,
                  })

@login_required
def demo(request, game_id):
    try:
        game = Game.objects.get(pk=game_id)
    except Exception, e:
        logging.error(e)

        return HttpResponseRedirect(reverse_lazy('drawing_host'))

    if request.method=='POST':
        if request.REQUEST.get('type')=='upload':
            form = ItemForm(request.REQUEST, request.FILES)
            if form.is_valid():
                item = form.save()
        elif request.REQUEST.get('type')=='next':
            item = Item.objects.filter(game_id=game_id).filter(is_active=True).order_by('-created_time')[0]
            item.number = cache.get(winner_key(item.pk))
            item.is_active = False
            item.save()

    items = Item.objects.filter(game_id=game_id).filter(is_active=True).order_by('-created_time')

    try:
        n_guests = get_n_guests(items[0].pk)    
    except:
        n_guests = 0

    return render(request, 'drawing/demo.html', {
                  'game': game,
                  'items': items,
                  'n_guests': n_guests,
                  })

@login_required
def drawing(request):
    item_id = request.REQUEST.get('item_id')
    import random
    number = random.randint(1, get_n_guests(item_id))
    cache.set(winner_key(item_id), number)

    return HttpResponse(json.dumps({
                        'status': 'success',
                        'number': number,
                        }))

@login_required
def n_guests(request):
    item_id = request.REQUEST.get('item_id')

    return HttpResponse(json.dumps({
                        'status': 'success',
                        'n_guests': get_n_guests(item_id),
                        }))

import redis
from django.conf import settings

redis = redis.from_url(settings.REDIS_URL)

def guest(request, game_id):
    item = Item.objects.filter(game_id=game_id).filter(is_active=True).order_by('-created_time')[0]
    item_key = 'item_%s' % (item.pk)
    number = request.session.get(item_key)
    if number is None:
        number = redis.incr(guest_key(item.pk))
        request.session[item_key] = number

    is_winner = str(cache.get(winner_key(item.pk)))==str(number)

    return render(request, 'drawing/guest.html', {
                  'item': item,
                  'number': number,
                  'is_winner': is_winner,
                  }) 


