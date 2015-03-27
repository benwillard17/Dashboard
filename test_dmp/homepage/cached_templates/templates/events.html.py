# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1427420346.845427
_enable_loop = True
_template_filename = 'C:\\Users\\benwillard17\\Documents\\GitHub\\Sprint3\\test_dmp\\homepage\\templates/events.html'
_template_uri = 'events.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content_right', 'content_left', 'content_center', 'content', 'title', 'jumbotron']


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
        def jumbotron():
            return render_jumbotron(context._locals(__M_locals))
        def content_right():
            return render_content_right(context._locals(__M_locals))
        def content_left():
            return render_content_left(context._locals(__M_locals))
        events = context.get('events', UNDEFINED)
        def content_center():
            return render_content_center(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        def title():
            return render_title(context._locals(__M_locals))
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
        def content():
            return render_content(context)
        events = context.get('events', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\t\t<!--create the table-->\r\n    <div class = "text-left">\r\n      <h2>Manage Events</h2>\r\n    </div>\r\n    <div class = "text-right">\r\n      <a href ="/homepage/events.create/" class= "btn btn-success">Create New Event</a>\r\n    </div>\r\n\t\t<table id="manage_table" class = "table table-striped table-bordered">\r\n\t\t    <tr>\r\n\t\t      <th>ID</th>\r\n\t\t      <th>Event Name</th>\r\n\t\t      <th>Start Date</th>\r\n          <th>End Date</th>\r\n\t\t      <th>Venue Name</th>\r\n          <th>City</th>\r\n\t\t      <th>Actions</th>\r\n\t\t    </tr>\r\n')
        for event in events:
            __M_writer('\t\t\t\t\t<tr>\r\n            <td> ')
            __M_writer(str( event.id ))
            __M_writer('</td>\r\n            <td> ')
            __M_writer(str( event.name ))
            __M_writer(' </td>\r\n\t\t\t\t\t\t<td> ')
            __M_writer(str( event.start_date ))
            __M_writer(' </td>\r\n\t\t\t\t\t\t<td> ')
            __M_writer(str( event.end_date ))
            __M_writer(' </td>\r\n\t\t\t\t\t\t<td> ')
            __M_writer(str( event.venue_name ))
            __M_writer(' </td>\r\n            <td> ')
            __M_writer(str( event.city ))
            __M_writer(' </td>\r\n\t\t\t\t\t\t<td width="1%" nowrap>\r\n\t\t\t\t\t\t\t<a class="label label-info" href="/homepage/events.edit/')
            __M_writer(str( event.id ))
            __M_writer('/">Edit</a>\r\n\t\t\t\t\t\t</td>\r\n\t\t\t\t\t</tr>\r\n')
        __M_writer('\t\t</table>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <title>CHF: Events</title>\r\n  ')
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


"""
__M_BEGIN_METADATA
{"uri": "events.html", "source_encoding": "ascii", "filename": "C:\\Users\\benwillard17\\Documents\\GitHub\\Sprint3\\test_dmp\\homepage\\templates/events.html", "line_map": {"128": 29, "65": 47, "130": 30, "131": 31, "132": 31, "133": 32, "70": 50, "129": 30, "136": 33, "137": 34, "138": 34, "75": 53, "140": 36, "141": 40, "60": 44, "81": 52, "147": 5, "139": 36, "171": 165, "87": 52, "153": 5, "27": 0, "93": 46, "159": 43, "165": 43, "99": 46, "134": 32, "105": 49, "135": 33, "45": 1, "111": 49, "50": 7, "117": 9, "55": 41, "124": 9, "125": 27, "126": 28, "127": 29}}
__M_END_METADATA
"""
