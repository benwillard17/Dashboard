# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425783829.113051
_enable_loop = True
_template_filename = 'C:\\Users\\benwillard17\\test_dmp\\homepage\\templates/events.html'
_template_uri = 'events.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content', 'jumbotron', 'content_left', 'content_right', 'content_center']


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
        def content():
            return render_content(context._locals(__M_locals))
        def jumbotron():
            return render_jumbotron(context._locals(__M_locals))
        def content_left():
            return render_content_left(context._locals(__M_locals))
        def content_center():
            return render_content_center(context._locals(__M_locals))
        def content_right():
            return render_content_right(context._locals(__M_locals))
        events = context.get('events', UNDEFINED)
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


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "filename": "C:\\Users\\benwillard17\\test_dmp\\homepage\\templates/events.html", "line_map": {"128": 48, "152": 146, "68": 49, "134": 48, "74": 5, "140": 45, "81": 5, "82": 23, "83": 24, "84": 25, "85": 25, "86": 26, "87": 26, "88": 27, "89": 27, "90": 28, "91": 28, "92": 29, "93": 29, "94": 30, "95": 30, "96": 32, "97": 32, "98": 36, "27": 0, "104": 39, "122": 42, "43": 1, "146": 45, "110": 39, "48": 37, "116": 42, "53": 40, "58": 43, "63": 46}, "uri": "events.html"}
__M_END_METADATA
"""
