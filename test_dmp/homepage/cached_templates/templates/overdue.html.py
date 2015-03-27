# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1427428788.811188
_enable_loop = True
_template_filename = 'C:\\Users\\benwillard17\\Documents\\GitHub\\Sprint3\\test_dmp\\homepage\\templates/overdue.html'
_template_uri = 'overdue.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content', 'content_right', 'title', 'content_left', 'jumbotron', 'content_center']


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
        def content_right():
            return render_content_right(context._locals(__M_locals))
        def title():
            return render_title(context._locals(__M_locals))
        def content_left():
            return render_content_left(context._locals(__M_locals))
        def jumbotron():
            return render_jumbotron(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        def content_center():
            return render_content_center(context._locals(__M_locals))
        overdues = context.get('overdues', UNDEFINED)
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
        __M_writer('\r\n<h2>Rented Items Overdue</h2>\r\n\t<div class = "text-right">\r\n      <a href ="/homepage/overdue/" class= "btn btn-success">Overdue Emails</a>\r\n  \t</div>\r\n\t\t<table id="manage_table" class = "table table-striped table-bordered">\r\n\t\t    <tr>\r\n\t\t      <th>ID</th>\r\n\t\t      <th>Condition</th>\r\n\t\t      <th>Due Date</th>\r\n\t\t      <th>Late Fee</th>\r\n\t\t    </tr>\r\n')
        for overdue in overdues:
            __M_writer('\t\t\t\t\t<tr>\r\n\t\t\t            <td> ')
            __M_writer(str( overdue[0] ))
            __M_writer('</td>\r\n\t\t\t            <td> ')
            __M_writer(str( overdue[1] ))
            __M_writer('</td>\r\n\t\t\t            <td> ')
            __M_writer(str( overdue[4] ))
            __M_writer('</td>\r\n\t\t\t            <td> $')
            __M_writer(str( overdue[3] ))
            __M_writer('</td>\r\n\t\t\t\t\t</tr>\r\n')
        __M_writer('\t\t</table>\r\n\r\n\r\n')
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


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <title>CHF: Overdue Rentals</title>\r\n  ')
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
{"uri": "overdue.html", "line_map": {"128": 37, "65": 38, "70": 41, "140": 34, "80": 9, "152": 40, "146": 34, "87": 9, "88": 21, "89": 22, "90": 23, "91": 23, "92": 24, "93": 24, "94": 25, "95": 25, "96": 26, "97": 26, "98": 29, "27": 0, "164": 158, "134": 37, "104": 43, "45": 1, "110": 43, "50": 7, "116": 5, "158": 40, "55": 32, "122": 5, "60": 35}, "filename": "C:\\Users\\benwillard17\\Documents\\GitHub\\Sprint3\\test_dmp\\homepage\\templates/overdue.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
