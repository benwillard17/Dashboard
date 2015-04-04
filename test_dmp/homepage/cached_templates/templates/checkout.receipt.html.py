# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428169365.947042
_enable_loop = True
_template_filename = 'C:\\Users\\benwillard17\\Documents\\GitHub\\Sprint3\\test_dmp\\homepage\\templates/checkout.receipt.html'
_template_uri = 'checkout.receipt.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['jumbotron', 'meta', 'title', 'content', 'content_center', 'content_left', 'content_right']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def meta():
            return render_meta(context._locals(__M_locals))
        icart = context.get('icart', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        items = context.get('items', UNDEFINED)
        pcart = context.get('pcart', UNDEFINED)
        def content_left():
            return render_content_left(context._locals(__M_locals))
        def content_right():
            return render_content_right(context._locals(__M_locals))
        def jumbotron():
            return render_jumbotron(context._locals(__M_locals))
        products = context.get('products', UNDEFINED)
        def title():
            return render_title(context._locals(__M_locals))
        def content_center():
            return render_content_center(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        amount = context.get('amount', UNDEFINED)
        str = context.get('str', UNDEFINED)
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


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        icart = context.get('icart', UNDEFINED)
        def content():
            return render_content(context)
        items = context.get('items', UNDEFINED)
        pcart = context.get('pcart', UNDEFINED)
        products = context.get('products', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        amount = context.get('amount', UNDEFINED)
        str = context.get('str', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\t\t<!--create the table-->\r\n    <div class = "text-left">\r\n      <h1>Thank You!</h1>\r\n    </div>\r\n    <p>Your purchase has been recorded and will be shipping soon!</p>\r\n    <p>You have been sent an email with details of this transaction.</p>\r\n\r\n    <form id= "loginform" method ="POST" action="/homepage/login.loginform/">\r\n  <h1>Shopping Cart</h1>\r\n    <table id="manage_table_shopping" class = "table table-striped table-bordered">\r\n      <thead>\r\n        <tr>\r\n          <th>Photo</th>\r\n          <th>Product Name</th>\r\n          <th>Quantity</th>\r\n          <th>Total</th>\r\n        </tr>\r\n      </thead>\r\n      <tbody>\r\n')
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


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"130": 13, "193": 76, "143": 13, "144": 33, "145": 34, "146": 34, "148": 34, "149": 36, "150": 36, "151": 36, "152": 36, "153": 37, "154": 37, "27": 0, "156": 38, "157": 39, "158": 39, "159": 42, "160": 53, "161": 54, "162": 54, "155": 38, "164": 54, "165": 56, "166": 56, "167": 56, "168": 56, "169": 57, "170": 57, "171": 58, "172": 58, "173": 61, "174": 65, "175": 65, "53": 1, "58": 7, "187": 79, "63": 11, "181": 79, "68": 71, "199": 76, "73": 74, "205": 82, "78": 77, "83": 80, "88": 83, "217": 211, "94": 73, "100": 73, "106": 9, "112": 9, "211": 82, "118": 5, "124": 5}, "uri": "checkout.receipt.html", "filename": "C:\\Users\\benwillard17\\Documents\\GitHub\\Sprint3\\test_dmp\\homepage\\templates/checkout.receipt.html"}
__M_END_METADATA
"""
