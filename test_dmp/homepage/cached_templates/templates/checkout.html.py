# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425790090.336202
_enable_loop = True
_template_filename = 'C:\\Users\\benwillard17\\test_dmp\\homepage\\templates/checkout.html'
_template_uri = 'checkout.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content_right', 'content', 'jumbotron', 'content_left', 'content_center']


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
        def content_right():
            return render_content_right(context._locals(__M_locals))
        def jumbotron():
            return render_jumbotron(context._locals(__M_locals))
        def content_left():
            return render_content_left(context._locals(__M_locals))
        def content_center():
            return render_content_center(context._locals(__M_locals))
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


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n\t<h2>Enter Checkout Information</h2>\r\n\t\t\t<form>\r\n\t\t\t\tCredit Card Number<br>\r\n\t\t\t\t<input type="text" name="Credit Card">\r\n\t\t\t\t<br>\r\n\t\t\t\tStreet Address<br>\r\n\t\t\t\t<input type="text" name="Address">\r\n\t\t\t\t<br>\r\n\t\t\t\tCity<br>\r\n\t\t\t\t<input type="text" name="City">\r\n\t\t\t\t<br>\r\n\t\t\t\tState<br>\r\n\t\t\t\t<input type="text" name="State">\r\n\t\t\t\t<br>\r\n\t\t\t\tZip<br>\r\n\t\t\t\t<input type="text" name="Zip">\r\n\t\t\t\t<br>\r\n\t\t\t</form><br>\r\n\t\t\t<a class="btn btn-success" href="/homepage/receipt">Complete Purchase</a>\r\n\t\t\t<a class="btn btn-default" href="/homepage/productlist">Cancel</a>\r\n')
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
{"line_map": {"97": 28, "67": 38, "133": 127, "103": 28, "73": 37, "42": 1, "109": 31, "47": 26, "79": 37, "27": 0, "115": 31, "52": 29, "85": 5, "121": 34, "57": 32, "91": 5, "62": 35, "127": 34}, "filename": "C:\\Users\\benwillard17\\test_dmp\\homepage\\templates/checkout.html", "uri": "checkout.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
