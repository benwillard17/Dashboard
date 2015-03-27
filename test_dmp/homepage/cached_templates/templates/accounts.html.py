# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1427414857.510037
_enable_loop = True
_template_filename = 'C:\\Users\\benwillard17\\Documents\\GitHub\\Sprint3\\test_dmp\\homepage\\templates/accounts.html'
_template_uri = 'accounts.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content_center', 'content', 'content_left', 'title', 'content_right', 'jumbotron']


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
        def content_center():
            return render_content_center(context._locals(__M_locals))
        def content_right():
            return render_content_right(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        def content_left():
            return render_content_left(context._locals(__M_locals))
        def title():
            return render_title(context._locals(__M_locals))
        user = context.get('user', UNDEFINED)
        def jumbotron():
            return render_jumbotron(context._locals(__M_locals))
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
        user = context.get('user', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\t\t<!--create the table-->\r\n    <div class = "text-left">\r\n      <h2>Manage Account</h2>\r\n    </div>\r\n\r\n\t\t<table id="manage_table" class = "table table-striped table-bordered">\r\n\t\t    <tr>\r\n\t\t      <th>Username</th>\r\n\t\t      <th>First Name</th>\r\n          \t  <th>Last Name</th>\r\n\t\t      <th>Email</th>\r\n\t\t      <th>Actions</th>\r\n\t\t    </tr>\r\n\t\t\t\t\t<tr>\r\n            \t\t\t<td> ')
        __M_writer(str( user.username ))
        __M_writer(' </td>\r\n\t\t\t\t\t\t<td> ')
        __M_writer(str( user.first_name ))
        __M_writer(' </td>\r\n\t\t\t\t\t\t<td> ')
        __M_writer(str( user.last_name ))
        __M_writer(' </td>\r\n\t\t\t\t\t\t<td> ')
        __M_writer(str( user.email ))
        __M_writer(' </td>\r\n\t\t\t\t\t\t<td width="1%" nowrap>\r\n\t\t\t\t\t\t<a class="label label-info" href="/homepage/accounts.edit/')
        __M_writer(str( user.id ))
        __M_writer('/">Edit Info</a><br>\r\n              \t\t\t<a class="label label-warning" href="/homepage/accounts.password/')
        __M_writer(str( user.id ))
        __M_writer('/">Change Password</a>\r\n\t\t\t\t\t\t</td>\r\n\t\t\t\t\t</tr>\r\n\t\t</table>\r\n')
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


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <title>CHF: Accounts</title>\r\n  ')
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


"""
__M_BEGIN_METADATA
{"line_map": {"65": 40, "130": 5, "70": 43, "136": 5, "75": 46, "142": 45, "109": 29, "81": 42, "148": 45, "124": 39, "87": 42, "154": 36, "27": 0, "93": 9, "160": 36, "100": 9, "101": 24, "102": 24, "103": 25, "104": 25, "105": 26, "106": 26, "107": 27, "108": 27, "45": 1, "110": 29, "111": 30, "112": 30, "50": 7, "118": 39, "55": 34, "60": 37, "166": 160}, "filename": "C:\\Users\\benwillard17\\Documents\\GitHub\\Sprint3\\test_dmp\\homepage\\templates/accounts.html", "source_encoding": "ascii", "uri": "accounts.html"}
__M_END_METADATA
"""
