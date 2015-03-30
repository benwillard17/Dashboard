# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1427753845.92615
_enable_loop = True
_template_filename = 'C:\\Users\\benwillard17\\Documents\\GitHub\\Sprint3\\test_dmp\\homepage\\templates/festivals.item.html'
_template_uri = 'festivals.item.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['title', 'content', 'jumbotron', 'content_right', 'content_center', 'content_left']


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
        saleitem = context.get('saleitem', UNDEFINED)
        def content_right():
            return render_content_right(context._locals(__M_locals))
        def content_center():
            return render_content_center(context._locals(__M_locals))
        def content_left():
            return render_content_left(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def title():
            return render_title(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        def jumbotron():
            return render_jumbotron(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'jumbotron'):
            context['self'].jumbotron(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

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
        __M_writer('\r\n    <title>CHF: Sale Item Detail</title>\r\n  ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        saleitem = context.get('saleitem', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n<div class = "text-left">\r\n      <h2>Sale Item Detail - ')
        __M_writer(str( saleitem.name ))
        __M_writer('</h2>\r\n    </div>\r\n\r\n    <div align="center">\r\n    \t<img height="450" src="')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage/media/')
        __M_writer(str( saleitem.photo ))
        __M_writer('" alt="">\r\n    </div>\r\n\t<table id="manage_table" class = "table table-striped table-bordered table-hover">\r\n\t\t    <tr>\r\n\t\t      <th>Description</th>\r\n\t\t      <th>Low Price</th>\r\n\t\t      <th>High Price</th>\r\n      \t \r\n\t\t    </tr>\r\n\t\t\t  <tr>\r\n          <td> ')
        __M_writer(str( saleitem.description ))
        __M_writer(' </td>\r\n          <td> ')
        __M_writer(str( saleitem.low_price ))
        __M_writer(' </td>\r\n\t\t      <td> $')
        __M_writer(str( saleitem.high_price ))
        __M_writer(' </td>\r\n         \r\n\t\t\t    </tr>\r\n\t\t</table>\r\n')
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
{"source_encoding": "ascii", "filename": "C:\\Users\\benwillard17\\Documents\\GitHub\\Sprint3\\test_dmp\\homepage\\templates/festivals.item.html", "line_map": {"66": 35, "131": 40, "71": 38, "167": 161, "137": 40, "143": 37, "81": 3, "125": 7, "110": 27, "87": 3, "27": 0, "93": 10, "161": 34, "155": 34, "101": 10, "102": 12, "103": 12, "104": 16, "105": 16, "106": 16, "107": 16, "108": 26, "109": 26, "46": 1, "111": 27, "112": 28, "113": 28, "51": 5, "119": 7, "56": 8, "61": 32, "149": 37}, "uri": "festivals.item.html"}
__M_END_METADATA
"""
