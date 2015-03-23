# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425794747.239721
_enable_loop = True
_template_filename = 'C:\\Users\\benwillard17\\test_dmp\\homepage\\templates/overdue.html'
_template_uri = 'overdue.html'
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
        overdues = context.get('overdues', UNDEFINED)
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


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        overdues = context.get('overdues', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n<h2>Rented Items Overdue</h2>\r\n\t\t<table id="manage_table" class = "table table-striped table-bordered">\r\n\t\t    <tr>\r\n\t\t      <th>ID</th>\r\n\t\t      <th>Name</th>\r\n\t\t      <th>Condition</th>\r\n\t\t      <th>Due Date</th>\r\n\t\t      <th>Late Fee</th>\r\n\t\t    </tr>\r\n')
        for overdue in overdues:
            __M_writer('\t\t\t\t\t<tr>\r\n\t\t\t            <td> ')
            __M_writer(str( overdue[0] ))
            __M_writer('</td>\r\n\t\t\t            <td> ')
            __M_writer(str( overdue[1] ))
            __M_writer('</td>\r\n\t\t\t            <td> ')
            __M_writer(str( overdue[2] ))
            __M_writer('</td>\r\n\t\t\t            <td> ')
            __M_writer(str( overdue[6] ))
            __M_writer('</td>\r\n\t\t\t            <td> $')
            __M_writer(str( overdue[5] ))
            __M_writer('</td>\r\n\t\t\t\t\t</tr>\r\n')
        __M_writer('\t\t</table>\r\n')
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
{"line_map": {"129": 33, "135": 30, "73": 27, "141": 30, "79": 27, "147": 141, "85": 5, "27": 0, "92": 5, "93": 15, "94": 16, "95": 17, "96": 17, "97": 18, "98": 18, "99": 19, "100": 19, "101": 20, "102": 20, "103": 21, "104": 21, "105": 24, "43": 1, "111": 36, "48": 25, "53": 28, "58": 31, "123": 33, "117": 36, "63": 34}, "filename": "C:\\Users\\benwillard17\\test_dmp\\homepage\\templates/overdue.html", "source_encoding": "ascii", "uri": "overdue.html"}
__M_END_METADATA
"""
