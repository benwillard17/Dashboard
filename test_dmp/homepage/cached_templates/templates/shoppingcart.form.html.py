# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1427573542.352089
_enable_loop = True
_template_filename = 'C:\\Users\\benwillard17\\Documents\\GitHub\\Sprint3\\test_dmp\\homepage\\templates/shoppingcart.form.html'
_template_uri = 'shoppingcart.form.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['jumbotron', 'content_right', 'content_left', 'content_center', 'content']


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
        products = context.get('products', UNDEFINED)
        def content_left():
            return render_content_left(context._locals(__M_locals))
        def jumbotron():
            return render_jumbotron(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        items = context.get('items', UNDEFINED)
        def content_center():
            return render_content_center(context._locals(__M_locals))
        amount = context.get('amount', UNDEFINED)
        def content_right():
            return render_content_right(context._locals(__M_locals))
        icart = context.get('icart', UNDEFINED)
        pcart = context.get('pcart', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        str = context.get('str', UNDEFINED)
        __M_writer = context.writer()
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


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        products = context.get('products', UNDEFINED)
        def content():
            return render_content(context)
        items = context.get('items', UNDEFINED)
        amount = context.get('amount', UNDEFINED)
        icart = context.get('icart', UNDEFINED)
        pcart = context.get('pcart', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        str = context.get('str', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n  <form id= "loginform" method ="POST" action="/homepage/login.loginform/">\r\n  <h2>Shopping Cart</h2>\r\n    <table id="manage_table_shopping" class = "table table-striped table-bordered">\r\n      <thead>\r\n        <tr>\r\n          <th>Photo</th>\r\n          <th>Product Name</th>\r\n          <th>Quantity</th>\r\n          <th>Total</th>\r\n          <th>Actions</th>\r\n        </tr>\r\n      </thead>\r\n      <tbody>\r\n')
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
            __M_writer('/" data-id="')
            __M_writer(str( p.id ))
            __M_writer('" class="btn btn-danger">Remove</a>\r\n            </td>\r\n          </tr>\r\n')
        __M_writer('      </tbody>\r\n  </table>\r\n  <table id="manage_table_shopping" class = "table table-striped table-bordered">\r\n      <thead>\r\n        <tr>\r\n          <th>Photo</th>\r\n          <th>Item Name</th>\r\n          <th>Total</th>\r\n          <th>Actions</th>\r\n        </tr>\r\n      </thead>\r\n      <tbody>\r\n')
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
            __M_writer('/" data-id="')
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
{"source_encoding": "ascii", "line_map": {"140": 3, "141": 17, "142": 18, "143": 18, "145": 18, "146": 20, "147": 20, "148": 20, "149": 20, "150": 21, "151": 21, "152": 22, "153": 22, "154": 23, "27": 0, "156": 25, "157": 25, "158": 25, "159": 25, "160": 29, "161": 41, "162": 42, "163": 42, "165": 42, "166": 44, "167": 44, "168": 44, "169": 44, "170": 45, "171": 45, "172": 46, "173": 46, "174": 48, "175": 48, "176": 48, "49": 1, "178": 52, "179": 56, "155": 23, "54": 64, "180": 56, "186": 180, "59": 67, "64": 70, "69": 73, "177": 48, "79": 66, "85": 66, "91": 75, "97": 75, "103": 69, "109": 69, "115": 72, "121": 72, "127": 3}, "filename": "C:\\Users\\benwillard17\\Documents\\GitHub\\Sprint3\\test_dmp\\homepage\\templates/shoppingcart.form.html", "uri": "shoppingcart.form.html"}
__M_END_METADATA
"""
