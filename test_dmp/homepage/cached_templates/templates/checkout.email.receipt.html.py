# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428198805.952245
_enable_loop = True
_template_filename = 'C:\\Users\\benwillard17\\Documents\\GitHub\\Sprint3\\test_dmp\\homepage\\templates/checkout.email.receipt.html'
_template_uri = 'checkout.email.receipt.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content_right', 'content_center', 'jumbotron', 'content_left', 'meta', 'content', 'title']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content_right():
            return render_content_right(context._locals(__M_locals))
        str = context.get('str', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        pcart = context.get('pcart', UNDEFINED)
        def jumbotron():
            return render_jumbotron(context._locals(__M_locals))
        amount = context.get('amount', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        def content_center():
            return render_content_center(context._locals(__M_locals))
        products = context.get('products', UNDEFINED)
        def meta():
            return render_meta(context._locals(__M_locals))
        def content_left():
            return render_content_left(context._locals(__M_locals))
        icart = context.get('icart', UNDEFINED)
        def title():
            return render_title(context._locals(__M_locals))
        items = context.get('items', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n<!--nothing to import-->\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer('\r\n\r\n  ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'meta'):
            context['self'].meta(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'jumbotron'):
            context['self'].jumbotron(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_left'):
            context['self'].content_left(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_center'):
            context['self'].content_center(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_right'):
            context['self'].content_right(**pageargs)
        

        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_right(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_right():
            return render_content_right(context)
        __M_writer = context.writer()
        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_center():
            return render_content_center(context)
        __M_writer = context.writer()
        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_jumbotron(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def jumbotron():
            return render_jumbotron(context)
        __M_writer = context.writer()
        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_left(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_left():
            return render_content_left(context)
        __M_writer = context.writer()
        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_meta(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def meta():
            return render_meta(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <meta name="Receipt" description="Customers get a receipt upon checkout" charset="UTF-8">\r\n  ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        str = context.get('str', UNDEFINED)
        pcart = context.get('pcart', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        amount = context.get('amount', UNDEFINED)
        def content():
            return render_content(context)
        products = context.get('products', UNDEFINED)
        icart = context.get('icart', UNDEFINED)
        items = context.get('items', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\t\t<!--create the table-->\r\n    <div class = "text-left">\r\n      <h1>Thank You!</h1>\r\n    </div>\r\n    <p>Your purchase has been recorded and will be shipping soon!</p>\r\n    <p>If you have rentals, please come to the CHF Office to pick them up and schedule a due date.</p>\r\n\r\n    <form id= "loginform" method ="POST" action="/homepage/login.loginform/">\r\n  <h1>Purchased Items</h1>\r\n    <table id="manage_table_shopping" class = "table table-striped table-bordered">\r\n      <thead>\r\n        <tr>\r\n          <th>Photo</th>\r\n          <th>Product Name</th>\r\n          <th>Quantity</th>\r\n          <th>Total</th>\r\n        </tr>\r\n      </thead>\r\n      <tbody>\r\n')
        for key in products:
            __M_writer('        ')
            p = products[key] 
            
            __M_writer('\r\n          <tr>\r\n            <td><img class="text-center" height="75" src="')
            __M_writer(str(STATIC_URL))
            __M_writer('homepage/media/')
            __M_writer(str( p.photo ))
            __M_writer('" alt=""></td>\r\n            <td>')
            __M_writer(str( p.name ))
            __M_writer('</td>\r\n            <td>')
            __M_writer(str( pcart[str(p.id)] ))
            __M_writer('</td>\r\n            <td>$ ')
            __M_writer(str( p.current_price * pcart[str(p.id)] ))
            __M_writer('</td>\r\n          </tr>\r\n')
        __M_writer('      </tbody>\r\n  </table>\r\n  <table id="manage_table_shopping" class = "table table-striped table-bordered">\r\n      <thead>\r\n        <tr>\r\n          <th>Photo</th>\r\n          <th>Item Name</th>\r\n          <th>Total</th>\r\n        </tr>\r\n      </thead>\r\n      <tbody>\r\n')
        for key in items:
            __M_writer('        ')
            i = items[key] 
            
            __M_writer('\r\n          <tr>\r\n            <td><img class="text-center" height="75" src="')
            __M_writer(str(STATIC_URL))
            __M_writer('homepage/media/')
            __M_writer(str( i.photo ))
            __M_writer('" alt=""></td>\r\n            <td>')
            __M_writer(str( i.name ))
            __M_writer('</td>\r\n            <td>$ ')
            __M_writer(str( i.standard_rental_price * icart[str(i.id)] ))
            __M_writer('</td>\r\n          </tr>\r\n')
        __M_writer('      </tbody>\r\n  </table>\r\n\r\n  <div id="Total" class="pull-right">\r\n  <h4>Total Amount: $')
        __M_writer(str( amount ))
        __M_writer('</h4>\r\n  </div>\r\n    <div class="btn-group">\r\n    </div>\r\n  </form>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <title>CHF: Receipt</title>\r\n  ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "checkout.email.receipt.html", "source_encoding": "ascii", "filename": "C:\\Users\\benwillard17\\Documents\\GitHub\\Sprint3\\test_dmp\\homepage\\templates/checkout.email.receipt.html", "line_map": {"131": 9, "137": 9, "143": 13, "16": 0, "185": 58, "47": 7, "156": 13, "157": 33, "158": 34, "159": 34, "161": 34, "162": 36, "163": 36, "164": 36, "165": 36, "166": 37, "167": 37, "168": 38, "169": 38, "170": 39, "171": 39, "172": 42, "173": 53, "174": 54, "175": 54, "177": 54, "178": 56, "179": 56, "180": 56, "181": 56, "182": 57, "183": 57, "184": 58, "52": 11, "186": 61, "187": 65, "188": 65, "62": 74, "194": 5, "67": 77, "72": 80, "77": 83, "206": 200, "83": 82, "57": 71, "89": 82, "95": 79, "101": 79, "107": 73, "125": 76, "113": 73, "119": 76, "200": 5, "42": 1}}
__M_END_METADATA
"""
