# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428158355.371066
_enable_loop = True
_template_filename = 'C:\\Users\\benwillard17\\Documents\\GitHub\\Sprint3\\test_dmp\\homepage\\templates/overdue.html'
_template_uri = 'overdue.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content_right', 'title', 'content_left', 'meta', 'content_center', 'content', 'jumbotron']


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
        def content_left():
            return render_content_left(context._locals(__M_locals))
        def content_center():
            return render_content_center(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        overdue1 = context.get('overdue1', UNDEFINED)
        def content_right():
            return render_content_right(context._locals(__M_locals))
        overdue3 = context.get('overdue3', UNDEFINED)
        overdue2 = context.get('overdue2', UNDEFINED)
        def meta():
            return render_meta(context._locals(__M_locals))
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


def render_meta(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def meta():
            return render_meta(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <meta name="Overdue Rentals" description="Info about overdue rentals can be found here" charset="UTF-8">\r\n  ')
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
        overdue3 = context.get('overdue3', UNDEFINED)
        overdue2 = context.get('overdue2', UNDEFINED)
        def content():
            return render_content(context)
        overdue1 = context.get('overdue1', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n<h1>Rented Items Overdue</h1>\r\n\t<div class = "text-right">\r\n      <a href ="/homepage/overdue.email/" class= "btn btn-success">Batch Email Overdue Rentals</a>\r\n  \t</div>\r\n  \t<h3>30 days</h3>\r\n\t\t<table id="manage_table" class = "table table-striped table-bordered">\r\n\t\t    <tr>\r\n\t\t      <th>Item Name</th>\r\n\t\t      <th>Due Date</th>\r\n\t\t      <th>First Name</th>\r\n\t\t      <th>Last Name</th>\r\n\t\t      <th>Email</th>\r\n\t\t    </tr>\r\n')
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
        __M_writer('\t\t</table>\r\n\t\t<h3>60 days</h3>\r\n\t\t<table id="manage_table" class = "table table-striped table-bordered">\r\n\t\t    <tr>\r\n\t\t      <th>Item Name</th>\r\n\t\t      <th>Due Date</th>\r\n\t\t      <th>First Name</th>\r\n\t\t      <th>Last Name</th>\r\n\t\t      <th>Email</th>\r\n\t\t    </tr>\r\n')
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
        __M_writer('\t\t</table>\r\n\t\t<h3>90 days</h3>\r\n\t\t<table id="manage_table" class = "table table-striped table-bordered">\r\n\t\t    <tr>\r\n\t\t      <th>Item Name</th>\r\n\t\t      <th>Due Date</th>\r\n\t\t      <th>First Name</th>\r\n\t\t      <th>Last Name</th>\r\n\t\t      <th>Email</th>\r\n\t\t    </tr>\r\n')
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
{"source_encoding": "ascii", "line_map": {"192": 69, "131": 9, "137": 84, "143": 84, "149": 13, "27": 0, "158": 13, "159": 27, "160": 28, "161": 29, "162": 29, "163": 30, "164": 30, "165": 31, "166": 31, "167": 32, "168": 32, "169": 33, "170": 33, "171": 36, "172": 46, "173": 47, "174": 48, "175": 48, "176": 49, "177": 49, "178": 50, "179": 50, "180": 51, "181": 51, "54": 7, "183": 52, "184": 55, "185": 65, "186": 66, "59": 11, "188": 67, "189": 68, "190": 68, "191": 69, "64": 76, "193": 70, "194": 70, "195": 71, "196": 71, "69": 79, "74": 82, "203": 78, "79": 85, "209": 78, "215": 209, "197": 74, "89": 87, "49": 1, "182": 52, "95": 87, "187": 67, "101": 5, "107": 5, "113": 81, "119": 81, "125": 9}, "filename": "C:\\Users\\benwillard17\\Documents\\GitHub\\Sprint3\\test_dmp\\homepage\\templates/overdue.html", "uri": "overdue.html"}
__M_END_METADATA
"""
