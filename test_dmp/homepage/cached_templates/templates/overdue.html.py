# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1427553233.076114
_enable_loop = True
_template_filename = 'C:\\Users\\benwillard17\\Documents\\GitHub\\Sprint3\\test_dmp\\homepage\\templates/overdue.html'
_template_uri = 'overdue.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content_left', 'content_right', 'content_center', 'title', 'jumbotron', 'content']


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
        def content_center():
            return render_content_center(context._locals(__M_locals))
        overdue3 = context.get('overdue3', UNDEFINED)
        def title():
            return render_title(context._locals(__M_locals))
        def jumbotron():
            return render_jumbotron(context._locals(__M_locals))
        def content_right():
            return render_content_right(context._locals(__M_locals))
        overdue2 = context.get('overdue2', UNDEFINED)
        overdue1 = context.get('overdue1', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
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
        overdue3 = context.get('overdue3', UNDEFINED)
        overdue2 = context.get('overdue2', UNDEFINED)
        overdue1 = context.get('overdue1', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n<h2>Rented Items Overdue</h2>\r\n\t<div class = "text-right">\r\n      <a href ="/homepage/overdue.email/" class= "btn btn-success">Batch Email Overdue Rentals</a>\r\n  \t</div>\r\n  \t<h3>30 days</h3>\r\n\t\t<table id="manage_table" class = "table table-striped table-bordered">\r\n\t\t    <tr>\r\n\t\t      <th>Name</th>\r\n\t\t      <th>Due Date</th>\r\n\t\t      <th>First Name</th>\r\n\t\t      <th>Last Name</th>\r\n\t\t      <th>Email</th>\r\n\t\t    </tr>\r\n')
        for overdue in overdue1:
            __M_writer('\t\t\t\t\t<tr>\r\n\t\t\t            <td> ')
            __M_writer(str( overdue[0] ))
            __M_writer('</td>\r\n\t\t\t            <td> ')
            __M_writer(str( overdue[1] ))
            __M_writer('</td>\r\n\t\t\t            <td> ')
            __M_writer(str( overdue[2] ))
            __M_writer('</td>\r\n\t\t\t            <td> ')
            __M_writer(str( overdue[3] ))
            __M_writer('</td>\r\n\t\t\t            <td> ')
            __M_writer(str( overdue[4] ))
            __M_writer('</td>\r\n\t\t\t\t\t</tr>\r\n')
        __M_writer('\t\t</table>\r\n\t\t<h3>60 days</h3>\r\n\t\t<table id="manage_table" class = "table table-striped table-bordered">\r\n\t\t    <tr>\r\n\t\t      <th>Name</th>\r\n\t\t      <th>Due Date</th>\r\n\t\t      <th>First Name</th>\r\n\t\t      <th>Last Name</th>\r\n\t\t      <th>Email</th>\r\n\t\t    </tr>\r\n')
        for overdue in overdue2:
            __M_writer('\t\t\t\t\t<tr>\r\n\t\t\t            <td> ')
            __M_writer(str( overdue[0] ))
            __M_writer('</td>\r\n\t\t\t            <td> ')
            __M_writer(str( overdue[1] ))
            __M_writer('</td>\r\n\t\t\t            <td> ')
            __M_writer(str( overdue[2] ))
            __M_writer('</td>\r\n\t\t\t            <td> ')
            __M_writer(str( overdue[3] ))
            __M_writer('</td>\r\n\t\t\t            <td> ')
            __M_writer(str( overdue[4] ))
            __M_writer('</td>\r\n\t\t\t\t\t</tr>\r\n')
        __M_writer('\t\t</table>\r\n\t\t<h3>90 days</h3>\r\n\t\t<table id="manage_table" class = "table table-striped table-bordered">\r\n\t\t    <tr>\r\n\t\t      <th>Name</th>\r\n\t\t      <th>Due Date</th>\r\n\t\t      <th>First Name</th>\r\n\t\t      <th>Last Name</th>\r\n\t\t      <th>Email</th>\r\n\t\t    </tr>\r\n')
        for overdue in overdue3:
            __M_writer('\t\t\t\t\t<tr>\r\n\t\t\t            <td> ')
            __M_writer(str( overdue[0] ))
            __M_writer('</td>\r\n\t\t\t            <td> ')
            __M_writer(str( overdue[1] ))
            __M_writer('</td>\r\n\t\t\t            <td> ')
            __M_writer(str( overdue[2] ))
            __M_writer('</td>\r\n\t\t\t            <td> ')
            __M_writer(str( overdue[3] ))
            __M_writer('</td>\r\n\t\t\t            <td> ')
            __M_writer(str( overdue[4] ))
            __M_writer('</td>\r\n\t\t\t\t\t</tr>\r\n')
        __M_writer('\t\t</table>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:\\Users\\benwillard17\\Documents\\GitHub\\Sprint3\\test_dmp\\homepage\\templates/overdue.html", "line_map": {"130": 74, "136": 74, "47": 1, "142": 9, "151": 9, "152": 23, "153": 24, "154": 25, "27": 0, "156": 26, "157": 26, "158": 27, "159": 27, "160": 28, "161": 28, "162": 29, "163": 29, "164": 32, "165": 42, "166": 43, "167": 44, "168": 44, "169": 45, "170": 45, "171": 46, "172": 46, "173": 47, "174": 47, "175": 48, "176": 48, "177": 51, "178": 61, "179": 62, "155": 25, "181": 63, "182": 64, "183": 64, "184": 65, "52": 7, "186": 66, "187": 66, "188": 67, "189": 67, "62": 75, "67": 78, "196": 190, "72": 81, "82": 77, "57": 72, "88": 77, "94": 83, "100": 83, "106": 80, "112": 80, "180": 63, "185": 65, "190": 70, "118": 5, "124": 5}, "source_encoding": "ascii", "uri": "overdue.html"}
__M_END_METADATA
"""
