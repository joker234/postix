import json
from decimal import Decimal

from postix.core.models import Cashdesk, Preorder, PreorderPosition, Product


class FakeStyle:

    def __getattribute__(self, name):
        return lambda x: print(x)


class FakeLog:
    def write(self, string):
        print(string)


def _build_product_dict(data, log, style):
    created_items = 0
    loaded_items = 0
    product_dict = dict()
    for item in data['items']:
        if item['variations']:
            log.write(style.ERROR('Warning: Import script cannot deal with variations yet!'))

        try:
            product = Product.objects.get(import_source_id=item['id'])
            loaded_items += 1
        except Product.DoesNotExist:
            product = Product(import_source_id=item['id'])
            product.price = Decimal(item['price'])
            product.tax_rate = Decimal(item['tax_rate'])
            created_items += 1
        product.name = item['name']
        product.save()
        product_dict[item['id']] = product

    log.write(style.SUCCESS(
        'Found {} new and {} known products in file.'.format(created_items, loaded_items)
    ))
    return product_dict


def import_pretix_data(data, add_cashdesks=False, log=FakeLog(), style=FakeStyle()):

    if isinstance(data, str):
        presale_export = json.loads(data)['event']
    else:
        presale_export = json.load(data)['event']

    log.write(style.NOTICE(
        'Importing data from event "{}".'.format(presale_export['name'])
    ))

    orders = presale_export['orders']
    product_dict = _build_product_dict(presale_export, log=log, style=style)

    created_orders = 0
    loaded_orders = 0
    for order in orders:
        preorder, created = Preorder.objects.get_or_create(
            order_code=order['code']
        )
        preorder.is_paid = (order['status'] == 'p')
        preorder.save()

        if not created:
            preorder_positions = {
                p.secret: p for p in preorder.positions.all()
            }
        else:
            preorder_positions = {}

        for position in order['positions']:
            if position['secret'] in preorder_positions:
                pp = preorder_positions[position['secret']]
                del preorder_positions[position['secret']]
            else:
                pp = PreorderPosition(preorder=preorder, secret=position['secret'])
            pp.product = product_dict[position['item']]
            pp.save()

        if preorder_positions:
            for pp in preorder_positions.values():
                pp.delete()

        created_orders += int(created)
        loaded_orders += int(not created)

    log.write(style.SUCCESS(
        'Found {} new and {} known orders in file.'.format(created_orders, loaded_orders)
    ))

    if add_cashdesks:
        cashdesk_count = add_cashdesks if isinstance(add_cashdesks, int) else 5
        for cashdesk_number in range(cashdesk_count):
            Cashdesk.objects.get_or_create(
                name='Cashdesk {}'.format(cashdesk_number + 1),
                ip_address='127.0.0.{}'.format(cashdesk_number + 1),
            )
        log.write(style.SUCCESS(
            'Added {} cashdesks.'.format(cashdesk_count)
        ))
    log.write(style.SUCCESS(
        'Import done.'
    ))
