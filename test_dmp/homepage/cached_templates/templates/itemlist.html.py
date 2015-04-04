# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428156237.062664
_enable_loop = True
_template_filename = 'C:\\Users\\benwillard17\\Documents\\GitHub\\Sprint3\\test_dmp\\homepage\\templates/itemlist.html'
_template_uri = 'itemlist.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['title', 'content', 'content_right', 'content_center', 'content_left', 'jumbotron', 'meta']


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
        def content_center():
            return render_content_center(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        def title():
            return render_title(context._locals(__M_locals))
        def content_left():
            return render_content_left(context._locals(__M_locals))
        def jumbotron():
            return render_jumbotron(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        items = context.get('items', UNDEFINED)
        def content_right():
            return render_content_right(context._locals(__M_locals))
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


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <title>CHF: Items</title>\r\n  ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        items = context.get('items', UNDEFINED)
        def content():
            return render_content(context)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n<h1>Items</h1>\r\n')
        for item in items:
            __M_writer('\t\t<div class="rental_container">\r\n      <a href="/homepage/itemlist.viewitem/')
            __M_writer(str( item.id ))
            __M_writer('/">\r\n      <div id="item" class="">')
            __M_writer(str( item ))
            __M_writer('</div>\r\n\t\t\t<img src="')
            __M_writer(str(STATIC_URL))
            __M_writer('homepage/media/')
            __M_writer(str( item.photo ))
            __M_writer('"/>\r\n\t\t\t\t<div id="current_price" class="">$')
            __M_writer(str( item.standard_rental_price ))
            __M_writer('</div>\r\n\t\t\t</a>\r\n\t\t\t<div class="text-right">\r\n\t\t\t\t<div class="row">\r\n              <div class="col-lg-12">\r\n                <div class="input-group">\r\n                  <span class="input-group-btn">\r\n                    <button id="item_')
            __M_writer(str( item.id))
            __M_writer('" class="btn btn-warning" data-iid="')
            __M_writer(str( item.id))
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


def render_meta(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def meta():
            return render_meta(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <meta name="Items" description="Customers can view rental items" charset="UTF-8">\r\n  ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:\\Users\\benwillard17\\Documents\\GitHub\\Sprint3\\test_dmp\\homepage\\templates/itemlist.html", "uri": "itemlist.html", "line_map": {"172": 35, "130": 52, "68": 44, "136": 52, "73": 47, "78": 50, "184": 7, "148": 49, "142": 49, "88": 3, "154": 46, "27": 0, "122": 25, "94": 3, "160": 46, "48": 1, "123": 25, "100": 11, "166": 35, "178": 7, "108": 11, "109": 13, "110": 14, "111": 15, "112": 15, "113": 16, "114": 16, "115": 17, "116": 17, "53": 5, "118": 17, "119": 18, "120": 18, "121": 25, "58": 9, "63": 33, "124": 25, "190": 184, "117": 17}, "source_encoding": "ascii"}
__M_END_METADATA
"""
