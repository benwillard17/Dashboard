# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1427334604.375764
_enable_loop = True
_template_filename = 'C:\\Users\\benwillard17\\Documents\\GitHub\\Sprint3\\test_dmp\\homepage\\templates/festivals.view.html'
_template_uri = 'festivals.view.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content_right', 'content_left', 'jumbotron', 'content', 'content_center']


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
    return runtime._inherit_from(context, 'basefestival.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        areas = context.get('areas', UNDEFINED)
        def jumbotron():
            return render_jumbotron(context._locals(__M_locals))
        def content_left():
            return render_content_left(context._locals(__M_locals))
        def content_center():
            return render_content_center(context._locals(__M_locals))
        def content_right():
            return render_content_right(context._locals(__M_locals))
        events = context.get('events', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
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


def render_content_left(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_left():
            return render_content_left(context)
        __M_writer = context.writer()
        __M_writer('\r\n\t\r\n')
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
        events = context.get('events', UNDEFINED)
        areas = context.get('areas', UNDEFINED)
        def content():
            return render_content(context)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\t<div id="festivalcontainer">\r\n\t\t<h2>Festival: ')
        __M_writer(str( events.name ))
        __M_writer(' </h2>\r\n\t\t<div class = "container-fluid">\r\n        \t<div class="row">\r\n        \t\t<div class="col-xs-4 bg-default">\r\n\t\t\t\t\t\r\n\t\t\t\t\t<h3>Areas</h3>\r\n\r\n\t\t\t\t\t<table id="manage_table" class = "table table-striped table-bordered">\r\n\r\n\t\t\t\t\t    <tr>\r\n\t\t\t\t\t      <th>Area Name</th>\r\n\t\t\t\t\t      <th>Description</th>\r\n\t\t\t          \t  <th>Place Number</th>\r\n\t\t\t\t\t      <th>Photo</th>\r\n\t\t\t\t\t      <th>Actions</th>\r\n\t\t\t\t\t    </tr>\r\n')
        for area in areas:
            __M_writer('\t\t\t\t\t\t\t\t<tr>\r\n\t\t\t            \t\t\t<td> ')
            __M_writer(str( area.name ))
            __M_writer(' </td>\r\n\t\t\t            \t\t\t<td> ')
            __M_writer(str( area.description ))
            __M_writer(' </td>\r\n\t\t\t            \t\t\t<td> ')
            __M_writer(str( area.place_number ))
            __M_writer(' </td>\r\n\t\t\t            \t\t\t<td> ')
            __M_writer(str( area.photo ))
            __M_writer(' </td>\r\n\t\t\t  \t\t\t\t\t\t<td width="1%" nowrap>\r\n\t\t\t\t\t\t\t\t\t\t<a class="label label-info" href="/homepage/festivals.area/')
            __M_writer(str( area.id ))
            __M_writer('">View</a>\r\n\t\t\t\t\t\t\t\t\t</td>\r\n\t\t\t\t\t\t\t\t</tr>\r\n')
        __M_writer('\t\t\t\t\t</table>\r\n\r\n\t\t\t\t\t<h3>Products</h3>\r\n\r\n\t\t\t\t\t<table id="manage_table" class = "table table-striped table-bordered">\r\n\r\n\t\t\t\t\t    <tr>\r\n\t\t\t\t\t      <th>Product Name</th>\r\n\t\t\t\t\t      <th>Description</th>\r\n\t\t\t          \t  <th>Place Number</th>\r\n\t\t\t\t\t      <th>Photo</th>\r\n\t\t\t\t\t      <th>Actions</th>\r\n\t\t\t\t\t    </tr>\r\n\t\t\t\t\t\t\t<!--%for  in : -->\r\n\t\t\t\t\t\t\t\t<tr>\r\n\t\t\t            \t\t\t<td> Hello </td>\r\n\t\t\t\t\t\t\t\t\t<td> Word </td>\r\n\t\t\t\t\t\t\t\t\t<td> 1 </td>\r\n\t\t\t\t\t\t\t\t\t<td> asdf.jpg </td>\r\n\t\t\t  \t\t\t\t\t\t<td width="1%" nowrap>\r\n\t\t\t\t\t\t\t\t\t\t<a class="label label-info" href="/homepage/festivals.view/">View</a>\r\n\t\t\t\t\t\t\t\t\t</td>\r\n\t\t\t\t\t\t\t\t</tr>\r\n\t\t\t\t\t\t\t<!-- %endfor -->\r\n\t\t\t\t\t</table>\r\n\r\n\t\t\t\t</div>\r\n\t\t\t\t<div class="col-xs-8 bg-default">\r\n\t\t\t\t\t<img width= "100%" src="')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage/media/autumn-in-park.jpg"/>\r\n\t\t\t\t\t<h3>Description</h3>\r\n\t\t\t\t\t<p> ')
        __M_writer(str( events.description ))
        __M_writer(' </p>\r\n\t\t\t\t</div>\r\n\t\t\t</div>\r\n\t\t</div>\r\n\t</div>\r\n')
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
{"source_encoding": "ascii", "uri": "festivals.view.html", "filename": "C:\\Users\\benwillard17\\Documents\\GitHub\\Sprint3\\test_dmp\\homepage\\templates/festivals.view.html", "line_map": {"128": 26, "65": 79, "130": 27, "131": 27, "132": 28, "133": 28, "70": 82, "129": 26, "136": 34, "137": 62, "138": 62, "139": 64, "76": 81, "152": 78, "82": 81, "88": 74, "27": 0, "94": 74, "100": 71, "134": 30, "146": 78, "140": 64, "60": 76, "106": 71, "135": 30, "45": 1, "112": 5, "50": 69, "158": 152, "55": 72, "121": 5, "122": 7, "123": 7, "124": 23, "125": 24, "126": 25, "127": 25}}
__M_END_METADATA
"""
