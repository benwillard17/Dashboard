# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428173971.144731
_enable_loop = True
_template_filename = 'C:\\Users\\benwillard17\\Documents\\GitHub\\Sprint3\\test_dmp\\homepage\\templates/festivals.view.html'
_template_uri = 'festivals.view.html'
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
    return runtime._inherit_from(context, 'basefestival.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def title():
            return render_title(context._locals(__M_locals))
        def content_center():
            return render_content_center(context._locals(__M_locals))
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
        events = context.get('events', UNDEFINED)
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
        __M_writer('\r\n    <title>CHF: Festivals</title>\r\n  ')
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
        __M_writer('\r\n    <meta name="Festivals" description="The different festivals one can attend" charset="UTF-8">\r\n  ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        events = context.get('events', UNDEFINED)
        areas = context.get('areas', UNDEFINED)
        def content():
            return render_content(context)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\t<div id="festivalcontainer">\r\n\t\t<h1>Festival: ')
        __M_writer(str( events.name ))
        __M_writer(' </h1>\r\n\t\t<div class = "container-fluid">\r\n        \t<div class="row">\r\n        \t\t<div class="col-xs-4 bg-default">\r\n\t\t\t\t\t\r\n\t\t\t\t\t<h3>Areas</h3>\r\n\r\n\t\t\t\t\t<table id="manage_table" class = "table table-striped table-bordered">\r\n\r\n\t\t\t\t\t    <tr>\r\n\t\t\t\t\t      <th>Area Name</th>\r\n\t\t\t\t\t      <th>Description</th>\r\n\t\t\t          \t  <th>Place Number</th>\r\n\t\t\t\t\t      <th>Photo</th>\r\n\t\t\t\t\t      <th>Actions</th>\r\n\t\t\t\t\t    </tr>\r\n')
        for area in areas:
            __M_writer('\t\t\t\t\t\t\t\t<tr>\r\n\t\t\t            \t\t\t<td> ')
            __M_writer(str( area.name ))
            __M_writer(' </td>\r\n\t\t\t            \t\t\t<td> ')
            __M_writer(str( area.description ))
            __M_writer(' </td>\r\n\t\t\t            \t\t\t<td> ')
            __M_writer(str( area.place_number ))
            __M_writer(' </td>\r\n\t\t\t            \t\t\t<td> <img width= "100%" src="')
            __M_writer(str(STATIC_URL))
            __M_writer('homepage/media/')
            __M_writer(str( area.photo ))
            __M_writer('"/> </td>\r\n\t\t\t  \t\t\t\t\t\t<td width="1%" nowrap>\r\n\t\t\t\t\t\t\t\t\t\t<a class="label label-info" href="/homepage/festivals.area/')
            __M_writer(str( area.id ))
            __M_writer('">View</a>\r\n\t\t\t\t\t\t\t\t\t</td>\r\n\t\t\t\t\t\t\t\t</tr>\r\n')
        __M_writer('\t\t\t\t\t</table>\r\n\r\n\t\t\r\n\t\t\t\t</div>\r\n\t\t\t\t<div class="col-xs-8 bg-default">\r\n\t\t\t\t\t<img width= "100%" src="')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage/media/')
        __M_writer(str( events.photo ))
        __M_writer('"/>\r\n\t\t\t\t\t<h3>Description</h3>\r\n\t\t\t\t\t<p> ')
        __M_writer(str( events.description ))
        __M_writer(' </p>\r\n\t\t\t\t</div>\r\n\t\t\t</div>\r\n\t\t</div>\r\n\t</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"192": 47, "132": 66, "138": 56, "144": 56, "150": 9, "27": 0, "156": 9, "162": 13, "49": 1, "171": 13, "172": 15, "173": 15, "174": 31, "175": 32, "176": 33, "177": 33, "178": 34, "179": 34, "180": 35, "181": 35, "182": 36, "183": 36, "184": 36, "185": 36, "186": 38, "187": 38, "188": 42, "189": 47, "190": 47, "191": 47, "64": 54, "193": 49, "194": 49, "69": 57, "200": 194, "74": 61, "79": 64, "84": 67, "90": 5, "54": 7, "96": 5, "59": 11, "102": 63, "108": 63, "114": 59, "120": 59, "126": 66}, "uri": "festivals.view.html", "source_encoding": "ascii", "filename": "C:\\Users\\benwillard17\\Documents\\GitHub\\Sprint3\\test_dmp\\homepage\\templates/festivals.view.html"}
__M_END_METADATA
"""
