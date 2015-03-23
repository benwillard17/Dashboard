# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425795416.527828
_enable_loop = True
_template_filename = 'C:\\Users\\benwillard17\\test_dmp\\homepage\\templates/productlist.html'
_template_uri = 'productlist.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['jumbotron', 'content', 'content_right', 'content_center', 'content_left']


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
        def content():
            return render_content(context._locals(__M_locals))
        def content_right():
            return render_content_right(context._locals(__M_locals))
        def jumbotron():
            return render_jumbotron(context._locals(__M_locals))
        def content_center():
            return render_content_center(context._locals(__M_locals))
        products = context.get('products', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
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
        __M_writer('\r\n<h2>Products</h2>\r\n')
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


"""
__M_BEGIN_METADATA
{"line_map": {"64": 43, "130": 42, "118": 45, "136": 42, "108": 16, "74": 28, "142": 39, "80": 28, "148": 39, "86": 3, "154": 148, "27": 0, "94": 3, "95": 5, "96": 6, "97": 7, "98": 7, "99": 8, "100": 8, "101": 9, "102": 9, "103": 9, "104": 9, "105": 10, "106": 10, "107": 16, "44": 1, "109": 18, "110": 18, "111": 18, "112": 18, "49": 26, "54": 37, "59": 40, "124": 45}, "filename": "C:\\Users\\benwillard17\\test_dmp\\homepage\\templates/productlist.html", "source_encoding": "ascii", "uri": "productlist.html"}
__M_END_METADATA
"""
