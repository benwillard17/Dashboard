# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1427154810.935066
_enable_loop = True
_template_filename = 'C:\\Users\\benwillard17\\Documents\\GitHub\\Sprint3\\test_dmp\\homepage\\templates/events.edit.html'
_template_uri = 'events.edit.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content_right', 'jumbotron', 'content_left', 'content', 'content_center']


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
        def jumbotron():
            return render_jumbotron(context._locals(__M_locals))
        form = context.get('form', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        event = context.get('event', UNDEFINED)
        def content_center():
            return render_content_center(context._locals(__M_locals))
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


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        form = context.get('form', UNDEFINED)
        def content():
            return render_content(context)
        event = context.get('event', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n<h2>Edit Event: ')
        __M_writer(str(event.name))
        __M_writer('</h2>\r\n\t<form class= "edit_table" method = "POST" >\r\n\r\n')
        __M_writer('\r\n')
        for field in form:
            __M_writer('        <div class="form-group">\r\n            <label for=')
            __M_writer(str(field.name))
            __M_writer('>')
            __M_writer(str(field.label))
            __M_writer(' ')
            __M_writer(str(field.errors))
            __M_writer('</label>\r\n            ')
            __M_writer(str( field ))
            __M_writer('\r\n        </div>\r\n')
        __M_writer('\t\t\t\t<hr>\r\n\t\t\t\t<button class="btn btn-success" type="submit">Submit</button>\r\n\t\t\t\t<a class="btn btn-default" href="/homepage/events">Cancel</a>\r\n\t\t\t\t<a href = "/homepage/events.delete/')
        __M_writer(str( event.id ))
        __M_writer('/" class="btn btn-danger pull-right">Delete</a>\r\n\t</form>\r\n')
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
{"filename": "C:\\Users\\benwillard17\\Documents\\GitHub\\Sprint3\\test_dmp\\homepage\\templates/events.edit.html", "line_map": {"64": 34, "128": 16, "130": 16, "131": 17, "132": 17, "69": 37, "134": 23, "129": 16, "75": 36, "141": 33, "59": 31, "81": 36, "147": 33, "87": 27, "153": 147, "27": 0, "93": 27, "133": 20, "99": 30, "105": 30, "135": 23, "44": 1, "111": 5, "49": 25, "54": 28, "119": 5, "120": 7, "121": 7, "122": 13, "123": 14, "124": 15, "125": 16, "126": 16, "127": 16}, "source_encoding": "ascii", "uri": "events.edit.html"}
__M_END_METADATA
"""
