# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1427336310.102302
_enable_loop = True
_template_filename = 'C:\\Users\\benwillard17\\Documents\\GitHub\\Sprint3\\test_dmp\\homepage\\templates/festivals.area.html'
_template_uri = 'festivals.area.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content', 'content_left', 'jumbotron', 'content_center', 'content_right']


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
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        products = context.get('products', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        def content_center():
            return render_content_center(context._locals(__M_locals))
        def content_right():
            return render_content_right(context._locals(__M_locals))
        def content_left():
            return render_content_left(context._locals(__M_locals))
        def jumbotron():
            return render_jumbotron(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n<!--nothing to import-->\r\n\r\n')
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


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        products = context.get('products', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\t<div id="festivalcontainer">\r\n\t\t<h2>Area </h2>\r\n\t\t<div class = "container-fluid">\r\n        \t<div class="row">\r\n        \t\t<div class="col-xs-12 bg-default">\r\n\t\t\t\t\t<img width= "100%" src="')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage/media/autumn-in-park.jpg"/>\r\n\t\t\t\t\t<h3>Description</h3>\r\n\t\t\t\t</div>\r\n\t\t\t</div>\r\n\t\t\t<div class="row">\r\n        \t\t<div class="col-xs-12 bg-default">\r\n\t\t\t\t\r\n        \t<h2>Products</h2>\r\n')
        for product in products:
            __M_writer('\t\t\t\t<div id="festivalproduct" class="item_container col-xs-2">\r\n\t\t\t\t\t\t<a href="/homepage/productlist.viewproduct/')
            __M_writer(str( product.id ))
            __M_writer('/">\r\n\t\t\t\t\t\t\t<div id="product" class="">')
            __M_writer(str( product.name ))
            __M_writer('</div>\r\n\t\t\t\t\t\t\t<img width = "100%" src="')
            __M_writer(str(STATIC_URL))
            __M_writer('homepage/media/')
            __M_writer(str( product.photo ))
            __M_writer('"/>\r\n\t\t\t\t\t\t\t\t<div id="current_price" class="">$')
            __M_writer(str( product.current_price ))
            __M_writer('</div>\r\n\t\t\t\t\t</a>\r\n\t\t\t\t</div>\r\n')
        __M_writer('\t\t</div>\r\n\t</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_left(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_left():
            return render_content_left(context)
        __M_writer = context.writer()
        __M_writer('\r\n\t\r\n')
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
{"uri": "festivals.area.html", "filename": "C:\\Users\\benwillard17\\Documents\\GitHub\\Sprint3\\test_dmp\\homepage\\templates/festivals.area.html", "source_encoding": "ascii", "line_map": {"64": 40, "128": 39, "69": 43, "134": 39, "75": 5, "140": 42, "152": 146, "146": 42, "83": 5, "84": 11, "85": 11, "86": 19, "87": 20, "88": 21, "89": 21, "90": 22, "27": 0, "92": 23, "93": 23, "94": 23, "95": 23, "96": 24, "97": 24, "98": 28, "91": 22, "104": 35, "44": 1, "110": 35, "49": 30, "116": 32, "54": 33, "122": 32, "59": 37}}
__M_END_METADATA
"""
