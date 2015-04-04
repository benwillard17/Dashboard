# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428158540.471768
_enable_loop = True
_template_filename = 'C:\\Users\\benwillard17\\Documents\\GitHub\\Sprint3\\test_dmp\\homepage\\templates/success.html'
_template_uri = 'success.html'
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
        emaillist = context.get('emaillist', UNDEFINED)
        def content_center():
            return render_content_center(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        def content_right():
            return render_content_right(context._locals(__M_locals))
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


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <title>CHF: Email Success</title>\r\n  ')
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
        __M_writer('\r\n    <meta name="Email" description="Email page denoting successfully sent emails" charset="UTF-8">\r\n  ')
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
        emaillist = context.get('emaillist', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n\t\t<!--create the table-->\r\n    <div class = "text-left">\r\n      <h1>Emails Successfully Sent</h1>\r\n    </div>\r\n    <h3>Overdue Rentals</h3>\r\n\r\n\t\t<table id="manage_table" class = "table table-striped table-bordered">\r\n\t\t    <tr>\r\n\t\t      <th>ID</th>\r\n\t\t      <th>Rental Item</th>\r\n\t\t      <th>Due Date</th>\r\n\t\t      <th>First Name</th>\r\n\t\t      <th>Last Name</th>\r\n\t\t      <th>Email</th>\r\n\t\t    </tr>\r\n')
        for user in emaillist:
            __M_writer('\t\t\t\t\t<tr>\r\n\t\t\t            <td> ')
            __M_writer(str( user[5] ))
            __M_writer('</td>\r\n\t\t\t            <td> ')
            __M_writer(str( user[0] ))
            __M_writer('</td>\r\n\t\t\t            <td> ')
            __M_writer(str( user[1] ))
            __M_writer('</td>\r\n\t\t\t            <td> ')
            __M_writer(str( user[2] ))
            __M_writer('</td>\r\n\t\t\t            <td> ')
            __M_writer(str( user[3] ))
            __M_writer('</td>\r\n\t\t\t            <td> ')
            __M_writer(str( user[4] ))
            __M_writer('</td>\r\n\t\t\t\t\t</tr>\r\n')
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


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"130": 9, "67": 43, "182": 42, "72": 46, "77": 49, "142": 48, "82": 52, "163": 33, "148": 13, "88": 51, "164": 34, "155": 13, "156": 29, "157": 30, "94": 51, "159": 31, "160": 32, "161": 32, "162": 33, "27": 0, "100": 5, "165": 34, "166": 35, "167": 35, "168": 36, "169": 36, "106": 5, "176": 42, "47": 1, "112": 45, "136": 48, "52": 7, "158": 31, "118": 45, "57": 11, "124": 9, "170": 39, "62": 40, "188": 182}, "filename": "C:\\Users\\benwillard17\\Documents\\GitHub\\Sprint3\\test_dmp\\homepage\\templates/success.html", "uri": "success.html"}
__M_END_METADATA
"""
