# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425779517.27631
_enable_loop = True
_template_filename = 'C:\\Users\\benwillard17\\test_dmp\\homepage\\templates/accounts.edit.html'
_template_uri = 'accounts.edit.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content', 'jumbotron', 'content_right', 'content_left', 'content_center']


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
        request = context.get('request', UNDEFINED)
        form = context.get('form', UNDEFINED)
        user = context.get('user', UNDEFINED)
        def content_left():
            return render_content_left(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        def jumbotron():
            return render_jumbotron(context._locals(__M_locals))
        def content_right():
            return render_content_right(context._locals(__M_locals))
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
        form = context.get('form', UNDEFINED)
        user = context.get('user', UNDEFINED)
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n<h2>Edit User: ')
        __M_writer(str(request.user.get_full_name()))
        __M_writer('</h2>\r\n\t<form class= "edit_table" method = "POST" >\r\n\r\n')
        __M_writer('\r\n')
        for field in form:
            __M_writer('        <div class="form-group">\r\n            <label for = ')
            __M_writer(str(field.name))
            __M_writer(' > ')
            __M_writer(str(field.label))
            __M_writer(' ')
            __M_writer(str(field.errors))
            __M_writer('</label>\r\n            ')
            __M_writer(str( field ))
            __M_writer('\r\n        </div>\r\n')
        __M_writer('\t\t\t\t<hr>\r\n\t\t\t\t<button class="btn btn-success" type="submit">Submit</button>\r\n        <a class="btn btn-warning" href="/homepage/accounts.password/')
        __M_writer(str( user.id ))
        __M_writer('/">Change Password</a>\r\n\t\t\t\t<a class="btn btn-default" href="/homepage/accounts">Cancel</a>\r\n\t\t\t\t<a href = "/homepage/accounts.delete/')
        __M_writer(str( user.id ))
        __M_writer('/" class="btn btn-danger pull-right">Delete</a>\r\n\t</form>\r\n')
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
{"filename": "C:\\Users\\benwillard17\\test_dmp\\homepage\\templates/accounts.edit.html", "source_encoding": "ascii", "uri": "accounts.edit.html", "line_map": {"65": 35, "133": 31, "70": 38, "139": 31, "76": 5, "109": 28, "145": 34, "99": 20, "85": 5, "86": 7, "87": 7, "88": 13, "89": 14, "90": 15, "91": 16, "92": 16, "93": 16, "94": 16, "95": 16, "96": 16, "97": 17, "98": 17, "27": 0, "100": 22, "101": 22, "102": 24, "103": 24, "151": 34, "45": 1, "157": 151, "50": 26, "115": 28, "55": 29, "121": 37, "60": 32, "127": 37}}
__M_END_METADATA
"""
