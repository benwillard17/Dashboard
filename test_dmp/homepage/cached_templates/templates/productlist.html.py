# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428170952.71608
_enable_loop = True
_template_filename = 'C:\\Users\\benwillard17\\Documents\\GitHub\\Sprint3\\test_dmp\\homepage\\templates/productlist.html'
_template_uri = 'productlist.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content_right', 'content_center', 'content_left', 'jumbotron', 'content', 'title', 'meta']


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
        def content_left():
            return render_content_left(context._locals(__M_locals))
        def jumbotron():
            return render_jumbotron(context._locals(__M_locals))
        def content_center():
            return render_content_center(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        def content_right():
            return render_content_right(context._locals(__M_locals))
        def title():
            return render_title(context._locals(__M_locals))
        def meta():
            return render_meta(context._locals(__M_locals))
        products = context.get('products', UNDEFINED)
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


def render_jumbotron(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def jumbotron():
            return render_jumbotron(context)
        __M_writer = context.writer()
        __M_writer('\r\n\t<form class="navbar-form navbar-left" role="search">\r\n        <div class="input-group">\r\n                <input type="text" class="form-control searchbar" placeholder="Search" name="srch-term" id="srch-term">\r\n                <div class="input-group-btn">\r\n                    <button class="btn btn-default" type="submit"><i class="glyphicon glyphicon-search"></i></button>\r\n                </div>\r\n            </div>\r\n          </form>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        products = context.get('products', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n<h1>Products</h1>\r\n')
        for product in products:
            __M_writer('\t\t<div class="item_container">\r\n      <a href="/homepage/productlist.viewproduct/')
            __M_writer(str( product.id ))
            __M_writer('/">\r\n      <div id="product" class="">')
            __M_writer(str( product ))
            __M_writer('</div>\r\n\t\t\t<img src="')
            __M_writer(str(STATIC_URL))
            __M_writer('homepage/media/')
            __M_writer(str( product.photo ))
            __M_writer('"/>\r\n\t\t\t\t<div id="current_price" class="">$')
            __M_writer(str( product.current_price ))
            __M_writer('</div>\r\n\t\t\t</a>\r\n\t\t\t<div class="text-right">\r\n\t\t\t\t<div class="row">\r\n              <div class="col-lg-12">\r\n                <div class="input-group">\r\n                  <input id="quantity_')
            __M_writer(str( product.id))
            __M_writer('" type="text" class="form-control" placeholder="Qty">\r\n                  <span class="input-group-btn">\r\n                    <button id="product_')
            __M_writer(str( product.id))
            __M_writer('" class="btn btn-warning" data-pid="')
            __M_writer(str( product.id))
            __M_writer('" type="button">Add to Cart</button>\r\n                  </span>\r\n                </div><!-- /input-group -->\r\n              </div><!-- /.col-lg-6 -->\r\n            </div><!-- /.row -->\r\n\t\t\t</div>\r\n\t\t</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <title>CHF: Products</title>\r\n  ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_meta(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def meta():
            return render_meta(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <meta name="Products" description="Management page for products" charset="UTF-8">\r\n  ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:\\Users\\benwillard17\\Documents\\GitHub\\Sprint3\\test_dmp\\homepage\\templates/productlist.html", "source_encoding": "ascii", "uri": "productlist.html", "line_map": {"192": 186, "130": 36, "68": 45, "186": 7, "158": 24, "136": 11, "73": 48, "78": 51, "144": 11, "145": 13, "146": 14, "147": 15, "148": 15, "149": 16, "150": 16, "151": 17, "88": 53, "153": 17, "152": 17, "27": 0, "156": 18, "154": 17, "94": 53, "159": 26, "160": 26, "48": 1, "162": 26, "155": 18, "100": 50, "168": 3, "161": 26, "106": 50, "174": 3, "157": 24, "112": 47, "180": 7, "53": 5, "118": 47, "58": 9, "124": 36, "63": 34}}
__M_END_METADATA
"""
