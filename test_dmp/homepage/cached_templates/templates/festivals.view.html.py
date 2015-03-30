# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1427752154.856878
_enable_loop = True
_template_filename = 'C:\\Users\\benwillard17\\Documents\\GitHub\\Sprint3\\test_dmp\\homepage\\templates/festivals.view.html'
_template_uri = 'festivals.view.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content', 'title', 'jumbotron', 'content_right', 'content_left', 'content_center']


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
        areas = context.get('areas', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        def content_center():
            return render_content_center(context._locals(__M_locals))
        events = context.get('events', UNDEFINED)
        def content_right():
            return render_content_right(context._locals(__M_locals))
        def jumbotron():
            return render_jumbotron(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def title():
            return render_title(context._locals(__M_locals))
        def content_left():
            return render_content_left(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n<!--nothing to import-->\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

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


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        areas = context.get('areas', UNDEFINED)
        def content():
            return render_content(context)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        events = context.get('events', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\t<div id="festivalcontainer">\r\n\t\t<h2>Festival: ')
        __M_writer(str( events.name ))
        __M_writer(' </h2>\r\n\t\t<div class = "container-fluid">\r\n        \t<div class="row">\r\n        \t\t<div class="col-xs-4 bg-default">\r\n\t\t\t\t\t\r\n\t\t\t\t\t<h3>Areas</h3>\r\n\r\n\t\t\t\t\t<table id="manage_table" class = "table table-striped table-bordered">\r\n\r\n\t\t\t\t\t    <tr>\r\n\t\t\t\t\t      <th>Area Name</th>\r\n\t\t\t\t\t      <th>Description</th>\r\n\t\t\t          \t  <th>Place Number</th>\r\n\t\t\t\t\t      <th>Photo</th>\r\n\t\t\t\t\t      <th>Actions</th>\r\n\t\t\t\t\t    </tr>\r\n')
        for area in areas:
            __M_writer('\t\t\t\t\t\t\t\t<tr>\r\n\t\t\t            \t\t\t<td> ')
            __M_writer(str( area.name ))
            __M_writer(' </td>\r\n\t\t\t            \t\t\t<td> ')
            __M_writer(str( area.description ))
            __M_writer(' </td>\r\n\t\t\t            \t\t\t<td> ')
            __M_writer(str( area.place_number ))
            __M_writer(' </td>\r\n\t\t\t            \t\t\t<td> ')
            __M_writer(str( area.photo ))
            __M_writer(' </td>\r\n\t\t\t  \t\t\t\t\t\t<td width="1%" nowrap>\r\n\t\t\t\t\t\t\t\t\t\t<a class="label label-info" href="/homepage/festivals.area/')
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
        __M_writer('\r\n\t\r\n')
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


"""
__M_BEGIN_METADATA
{"uri": "festivals.view.html", "source_encoding": "ascii", "line_map": {"67": 57, "155": 55, "161": 55, "72": 60, "137": 52, "111": 43, "77": 63, "143": 62, "173": 59, "167": 59, "83": 9, "149": 62, "27": 0, "92": 9, "93": 11, "94": 11, "95": 27, "96": 28, "97": 29, "98": 29, "99": 30, "100": 30, "101": 31, "102": 31, "103": 32, "104": 32, "105": 34, "106": 34, "107": 38, "108": 43, "109": 43, "110": 43, "47": 1, "112": 45, "113": 45, "179": 173, "52": 7, "131": 52, "119": 5, "57": 50, "125": 5, "62": 53}, "filename": "C:\\Users\\benwillard17\\Documents\\GitHub\\Sprint3\\test_dmp\\homepage\\templates/festivals.view.html"}
__M_END_METADATA
"""
