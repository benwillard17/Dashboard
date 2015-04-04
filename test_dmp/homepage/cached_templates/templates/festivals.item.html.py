# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428174803.890923
_enable_loop = True
_template_filename = 'C:\\Users\\benwillard17\\Documents\\GitHub\\Sprint3\\test_dmp\\homepage\\templates/festivals.item.html'
_template_uri = 'festivals.item.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['jumbotron', 'content_left', 'content', 'content_right', 'meta', 'content_center', 'title']


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
        saleitem = context.get('saleitem', UNDEFINED)
        user = context.get('user', UNDEFINED)
        def meta():
            return render_meta(context._locals(__M_locals))
        def title():
            return render_title(context._locals(__M_locals))
        def jumbotron():
            return render_jumbotron(context._locals(__M_locals))
        def content_right():
            return render_content_right(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def content_center():
            return render_content_center(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer('\r\n\r\n  ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'meta'):
            context['self'].meta(**pageargs)
        

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


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        user = context.get('user', UNDEFINED)
        def content():
            return render_content(context)
        saleitem = context.get('saleitem', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n<div class = "text-left">\r\n      <h1>Sale Item Detail - ')
        __M_writer(str( saleitem.name ))
        __M_writer('</h1>\r\n    </div>\r\n\r\n    <div align="center">\r\n    \t<img height="450" src="')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage/media/')
        __M_writer(str( saleitem.photo ))
        __M_writer('" alt="">\r\n    </div>\r\n\t<table id="manage_table" class = "table table-striped table-bordered table-hover">\r\n\t\t    <tr>\r\n\t\t      <th>Description</th>\r\n\t\t      <th>Low Price</th>\r\n          <th>High Price</th>\r\n\t\t      <th>Artisan</th>\r\n\t\t    </tr>\r\n\t\t\t  <tr>\r\n          <td> ')
        __M_writer(str( saleitem.description ))
        __M_writer(' </td>\r\n          <td> $')
        __M_writer(str( saleitem.low_price ))
        __M_writer(' </td>\r\n          <td> $')
        __M_writer(str( saleitem.high_price ))
        __M_writer(' </td>\r\n\t\t      <td> ')
        __M_writer(str( user.first_name ))
        __M_writer(' ')
        __M_writer(str(user.last_name))
        __M_writer('</td>\r\n         \r\n\t\t\t    </tr>\r\n\t\t</table>\r\n')
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


def render_meta(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def meta():
            return render_meta(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <meta name="Sale Items" description="Customers can view info about sale items here" charset="UTF-8">\r\n  ')
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


"""
__M_BEGIN_METADATA
{"uri": "festivals.item.html", "line_map": {"64": 12, "128": 20, "130": 30, "131": 31, "132": 31, "69": 37, "134": 32, "129": 30, "136": 33, "137": 33, "74": 40, "138": 33, "79": 43, "144": 45, "150": 45, "89": 11, "27": 0, "135": 33, "186": 3, "95": 11, "133": 32, "162": 7, "59": 9, "101": 39, "49": 1, "168": 42, "156": 7, "107": 39, "174": 42, "113": 14, "192": 186, "180": 3, "54": 5, "122": 14, "123": 16, "124": 16, "125": 20, "126": 20, "127": 20}, "filename": "C:\\Users\\benwillard17\\Documents\\GitHub\\Sprint3\\test_dmp\\homepage\\templates/festivals.item.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
