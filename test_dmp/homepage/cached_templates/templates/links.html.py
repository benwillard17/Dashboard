# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428105252.125352
_enable_loop = True
_template_filename = 'C:\\Users\\benwillard17\\Documents\\GitHub\\Sprint3\\test_dmp\\homepage\\templates/links.html'
_template_uri = 'links.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['meta', 'content_left', 'content_center', 'content_right', 'content', 'jumbotron', 'title']


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
        def meta():
            return render_meta(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        def content_center():
            return render_content_center(context._locals(__M_locals))
        def content_left():
            return render_content_left(context._locals(__M_locals))
        def content_right():
            return render_content_right(context._locals(__M_locals))
        def jumbotron():
            return render_jumbotron(context._locals(__M_locals))
        def title():
            return render_title(context._locals(__M_locals))
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


def render_meta(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def meta():
            return render_meta(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <meta name="Links" description="Links to other websites" charset="UTF-8">\r\n  ')
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
        __M_writer('\r\n\r\n  <div class = "text-left">\r\n    <h1>Check out these other websites!</h1>\r\n  </div>\r\n  <div>\r\n  \t<ul id="link">\r\n  \t\t<li><a href ="http://www.americaslibrary.gov/">Americas Library</a></li>\r\n  \t\t<li><a href ="http://www.history.com/">History</a></li>\r\n  \t\t<li><a href ="www.landofthebrave.info/"> Land of the Brave</a></li>\r\n  \t\t<li><a href ="http://www.uncp.edu/">UNCP</a></li>\r\n  \t\t<li><a href ="http://www.ducksters.com/history/colonial_america/">Ducksters</a></li>\r\n  \t</ul>\r\n')
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


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <title>CHF: Links</title>\r\n  ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "links.html", "line_map": {"129": 37, "66": 29, "171": 165, "71": 32, "76": 35, "141": 13, "81": 38, "147": 28, "87": 9, "153": 28, "27": 0, "93": 9, "159": 5, "99": 31, "165": 5, "105": 31, "135": 13, "46": 1, "111": 34, "51": 7, "117": 34, "56": 11, "123": 37, "61": 26}, "source_encoding": "ascii", "filename": "C:\\Users\\benwillard17\\Documents\\GitHub\\Sprint3\\test_dmp\\homepage\\templates/links.html"}
__M_END_METADATA
"""
