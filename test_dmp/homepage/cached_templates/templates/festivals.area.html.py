# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428174721.675644
_enable_loop = True
_template_filename = 'C:\\Users\\benwillard17\\Documents\\GitHub\\Sprint3\\test_dmp\\homepage\\templates/festivals.area.html'
_template_uri = 'festivals.area.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['title', 'content_center', 'content_left', 'content_right', 'jumbotron', 'meta', 'content']


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
        def title():
            return render_title(context._locals(__M_locals))
        def content_center():
            return render_content_center(context._locals(__M_locals))
        saleitem = context.get('saleitem', UNDEFINED)
        def content_left():
            return render_content_left(context._locals(__M_locals))
        def content_right():
            return render_content_right(context._locals(__M_locals))
        areas = context.get('areas', UNDEFINED)
        def meta():
            return render_meta(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def jumbotron():
            return render_jumbotron(context._locals(__M_locals))
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


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <title>CHF: Festival Areas</title>\r\n  ')
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
        __M_writer('\r\n\t\r\n')
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
        __M_writer('\r\n    <meta name="Festival Areas" description="People can view areas and festivals" charset="UTF-8">\r\n  ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        areas = context.get('areas', UNDEFINED)
        saleitem = context.get('saleitem', UNDEFINED)
        def content():
            return render_content(context)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\t<div id="festivalcontainer">\r\n\t\t<h1>Area: ')
        __M_writer(str( areas.name ))
        __M_writer(' </h1>\r\n\t\t<div class = "container-fluid">\r\n        \t<div class="row">\r\n        \t\t<div class="col-xs-12 bg-default">\r\n\t\t\t\t\t<img width= "100%" src="')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage/media/')
        __M_writer(str( areas.photo ))
        __M_writer('"/>\r\n\t\t\t\t\t<h3>Description</h3>\r\n\t\t\t\t\t<p>')
        __M_writer(str( areas.description ))
        __M_writer('</p>\r\n\t\t\t\t</div>\r\n\t\t\t</div>\r\n\t\t\t<div class="row">\r\n        \t\t<div class="col-xs-12 bg-default">\r\n\t\t\t\t\r\n        \t<h2>Sale Items</h2>\r\n')
        for si in saleitem:
            __M_writer('\t\t\t\t<div id="festivalproduct" class="item_container col-xs-2">\r\n\t\t\t\t\t\t<a href="/homepage/festivals.item/')
            __M_writer(str( si.id ))
            __M_writer('/">\r\n\t\t\t\t\t\t\t<div id="product" class="">')
            __M_writer(str( si.name ))
            __M_writer('</div>\r\n\t\t\t\t\t\t\t<img width = "100%" src="')
            __M_writer(str(STATIC_URL))
            __M_writer('homepage/media/')
            __M_writer(str( si.photo ))
            __M_writer('"/>\r\n\t\t\t\t\t\t\t\t<div id="current_price" class="">$')
            __M_writer(str( si.high_price ))
            __M_writer('</div>\r\n\t\t\t\t\t</a>\r\n\t\t\t\t</div>\r\n')
        __M_writer('\t\t</div>\r\n\t</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"192": 37, "132": 51, "138": 41, "144": 41, "150": 9, "27": 0, "156": 9, "162": 13, "49": 1, "171": 13, "172": 15, "173": 15, "174": 19, "175": 19, "176": 19, "177": 19, "178": 21, "179": 21, "180": 28, "181": 29, "182": 30, "183": 30, "184": 31, "185": 31, "186": 32, "187": 32, "188": 32, "189": 32, "190": 33, "191": 33, "64": 39, "69": 42, "198": 192, "74": 46, "79": 49, "84": 52, "90": 5, "54": 7, "96": 5, "59": 11, "102": 48, "108": 48, "114": 44, "120": 44, "126": 51}, "uri": "festivals.area.html", "source_encoding": "ascii", "filename": "C:\\Users\\benwillard17\\Documents\\GitHub\\Sprint3\\test_dmp\\homepage\\templates/festivals.area.html"}
__M_END_METADATA
"""
