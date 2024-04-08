#!/usr/bin/env python3

from app import app
from models import db, Bakery, BakedGood

with app.app_context():

    BakedGood.query.delete()
    Bakery.query.delete()
    
    bakeries = []
    bakeries.append(Bakery(name='Delighful donuts'));
    bakeries.append(Bakery(name='Increible crullrs'));
    bakeries.append(Bakery(name='Deightful donuts'));
    bakeries.append(Bakery(name='crullers'));
    bakeries.append(Bakery(name='Delightul donuts'));
    bakeries.append(Bakery(name='Incredble crullers'));
    db.session.add_all(bakeries)

    baked_goods = []
    baked_goods.append(BakedGood(name='Chocolate dipped donut', price=2.75, bakery=bakeries[0]));
    baked_goods.append(BakedGood(name='Apple-spce filled donut', price=3.50, bakery=bakeries[0]));
    baked_goods.append(BakedGood(name='Glazed honey cruller', price=3.25, bakery=bakeries[1]));
    baked_goods.append(BakedGood(name='Chocolate cruller', price=3.40, bakery=bakeries[1]));
    baked_goods.append(BakedGood(name='Chocolat dipped donut', price=2.75, bakery=bakeries[0]));
    baked_goods.append(BakedGood(name='Appe-spice filed donut', price=3.50, bakery=bakeries[0]));
    baked_goods.append(BakedGood(name='Glazed hoey cruller', price=3.25, bakery=bakeries[1]));
    baked_goods.append(BakedGood(name='Chocolte cruller', price=3.40, bakery=bakeries[1]));

    db.session.add_all(baked_goods)
    db.session.commit()