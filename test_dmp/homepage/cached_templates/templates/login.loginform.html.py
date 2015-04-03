# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428098440.719977
_enable_loop = True
_template_filename = 'C:\\Users\\benwillard17\\Documents\\GitHub\\Sprint3\\test_dmp\\homepage\\templates/login.loginform.html'
_template_uri = 'login.loginform.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['title', 'content']


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
    return runtime._inherit_from(context, 'base_ajax.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        form = context.get('form', UNDEFINED)
        def title():
            return render_title(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

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
        __M_writer('\r\n    <title>CHF: Login</title>\r\n  ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        form = context.get('form', UNDEFINED)
        def title():
            return render_title(context)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer('\r\n\r\n  <div id= "loginform_container" align="center">\r\n    <form id= "loginform" method ="POST" action="/homepage/login.loginform/">\r\n      <table>\r\n        ')
        __M_writer(str( form ))
        __M_writer('\r\n      </table>\r\n      <div id="submit_button_container" align="center">\r\n        <button id="submit_button" class="btn btn-warning" type="submit">Login</button>\r\n        <a href="/password_reset/">Forgot Password?</a>\r\n      </div>\r\n    </form>\r\n  </div>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:\\Users\\benwillard17\\Documents\\GitHub\\Sprint3\\test_dmp\\homepage\\templates/login.loginform.html", "source_encoding": "ascii", "line_map": {"48": 5, "82": 76, "75": 12, "37": 1, "54": 5, "76": 12, "42": 21, "27": 0, "60": 3, "74": 7, "69": 3}, "uri": "login.loginform.html"}
__M_END_METADATA
"""
