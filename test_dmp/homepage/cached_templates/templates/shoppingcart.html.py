# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428156246.141116
_enable_loop = True
_template_filename = 'C:\\Users\\benwillard17\\Documents\\GitHub\\Sprint3\\test_dmp\\homepage\\templates/shoppingcart.html'
_template_uri = 'shoppingcart.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content', 'title', 'meta']


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
    return runtime._inherit_from(context, 'base_ajax.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        products = context.get('products', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        def title():
            return render_title(context._locals(__M_locals))
        icart = context.get('icart', UNDEFINED)
        str = context.get('str', UNDEFINED)
        pcart = context.get('pcart', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        items = context.get('items', UNDEFINED)
        amount = context.get('amount', UNDEFINED)
        def meta():
            return render_meta(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer('\r\n\r\n  ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'meta'):
            context['self'].meta(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        products = context.get('products', UNDEFINED)
        def content():
            return render_content(context)
        icart = context.get('icart', UNDEFINED)
        str = context.get('str', UNDEFINED)
        pcart = context.get('pcart', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        items = context.get('items', UNDEFINED)
        amount = context.get('amount', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n  <form id= "loginform" method ="POST" action="/homepage/login.loginform/">\r\n    <h2>Products</h2>\r\n    <table id="manage_table_shopping" class = "table table-striped table-bordered">\r\n      <thead>\r\n        <tr>\r\n          <th>Photo</th>\r\n          <th>Product Name</th>\r\n          <th>Quantity</th>\r\n          <th>Total</th>\r\n          <th>Actions</th>\r\n        </tr>\r\n      </thead>\r\n      <tbody>\r\n')
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
            __M_writer('</td>\r\n            <td width="15%" nowrap>\r\n              <a href="/homepage/shoppingcart.delete/')
            __M_writer(str( p.id ))
            __M_writer('/product" data-id="')
            __M_writer(str( p.id ))
            __M_writer('" class="btn btn-danger">Remove</a>\r\n            </td>\r\n          </tr>\r\n')
        __M_writer('      </tbody>\r\n  </table>\r\n  <h2>Items</h2>\r\n  <table id="manage_table_shopping" class = "table table-striped table-bordered">\r\n      <thead>\r\n        <tr>\r\n          <th>Photo</th>\r\n          <th>Item Name</th>\r\n          <th>Total</th>\r\n          <th>Actions</th>\r\n        </tr>\r\n      </thead>\r\n      <tbody>\r\n')
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
            __M_writer('</td>\r\n            <td width="15%" nowrap>\r\n              <a href="/homepage/shoppingcart.delete/')
            __M_writer(str( i.id ))
            __M_writer('/item" data-id="')
            __M_writer(str( i.id ))
            __M_writer('" class="btn btn-danger">Remove</a>\r\n            </td>\r\n          </tr>\r\n')
        __M_writer('      </tbody>\r\n  </table>\r\n\r\n  <div id="Total" class="pull-right">\r\n  <h4>Total Amount: $')
        __M_writer(str( amount ))
        __M_writer('</h4>\r\n  </div>\r\n    <div class="btn-group">\r\n      <form method="POST">\r\n        <a class="btn btn-warning" type="Submit" href="/homepage/checkout/">Checkout</a>\r\n      </form>\r\n    </div>\r\n  </form>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <title>CHF: Shopping Cart</title>\r\n  ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_meta(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def meta():
            return render_meta(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <meta name="Shopping Cart" description="Shopping Cart" charset="UTF-8">\r\n  ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:\\Users\\benwillard17\\Documents\\GitHub\\Sprint3\\test_dmp\\homepage\\templates/shoppingcart.html", "uri": "shoppingcart.html", "line_map": {"130": 3, "136": 7, "142": 7, "148": 142, "27": 0, "45": 1, "50": 5, "55": 9, "65": 11, "78": 11, "79": 25, "80": 26, "81": 26, "83": 26, "84": 28, "85": 28, "86": 28, "87": 28, "88": 29, "89": 29, "90": 30, "91": 30, "92": 31, "93": 31, "94": 33, "95": 33, "96": 33, "97": 33, "98": 37, "99": 50, "100": 51, "101": 51, "103": 51, "104": 53, "105": 53, "106": 53, "107": 53, "108": 54, "109": 54, "110": 55, "111": 55, "112": 57, "113": 57, "114": 57, "115": 57, "116": 61, "117": 65, "118": 65, "124": 3}, "source_encoding": "ascii"}
__M_END_METADATA
"""
