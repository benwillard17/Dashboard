# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1427758296.601165
_enable_loop = True
_template_filename = 'C:\\Users\\benwillard17\\Documents\\GitHub\\Sprint3\\test_dmp\\homepage\\templates/shoppingcart.html'
_template_uri = 'shoppingcart.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content']


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
        def content():
            return render_content(context._locals(__M_locals))
        pcart = context.get('pcart', UNDEFINED)
        items = context.get('items', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        products = context.get('products', UNDEFINED)
        amount = context.get('amount', UNDEFINED)
        icart = context.get('icart', UNDEFINED)
        str = context.get('str', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        pcart = context.get('pcart', UNDEFINED)
        items = context.get('items', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        products = context.get('products', UNDEFINED)
        amount = context.get('amount', UNDEFINED)
        icart = context.get('icart', UNDEFINED)
        str = context.get('str', UNDEFINED)
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


"""
__M_BEGIN_METADATA
{"line_map": {"64": 3, "65": 17, "66": 18, "67": 18, "69": 18, "70": 20, "71": 20, "72": 20, "73": 20, "74": 21, "75": 21, "76": 22, "77": 22, "78": 23, "79": 23, "80": 25, "81": 25, "82": 25, "83": 25, "84": 29, "85": 42, "86": 43, "87": 43, "89": 43, "90": 45, "27": 0, "92": 45, "93": 45, "94": 46, "95": 46, "96": 47, "97": 47, "98": 49, "91": 45, "100": 49, "101": 49, "102": 53, "103": 57, "104": 57, "41": 1, "110": 104, "99": 49, "51": 3}, "filename": "C:\\Users\\benwillard17\\Documents\\GitHub\\Sprint3\\test_dmp\\homepage\\templates/shoppingcart.html", "source_encoding": "ascii", "uri": "shoppingcart.html"}
__M_END_METADATA
"""
