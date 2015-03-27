# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1427414670.960418
_enable_loop = True
_template_filename = 'C:\\Users\\benwillard17\\Documents\\GitHub\\Sprint3\\test_dmp\\homepage\\templates/productlist.viewproduct.html'
_template_uri = 'productlist.viewproduct.html'
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
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def content_center():
            return render_content_center(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        product = context.get('product', UNDEFINED)
        def content_right():
            return render_content_right(context._locals(__M_locals))
        def content_left():
            return render_content_left(context._locals(__M_locals))
        def title():
            return render_title(context._locals(__M_locals))
        def jumbotron():
            return render_jumbotron(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'jumbotron'):
            context['self'].jumbotron(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

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
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def content():
            return render_content(context)
        product = context.get('product', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n<div class = "text-left">\r\n      <h2>Product Detail - ')
        __M_writer(str( product.name ))
        __M_writer('</h2>\r\n    </div>\r\n\r\n    <div align="center">\r\n    \t<img height="450" src="')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage/media/')
        __M_writer(str( product.photo ))
        __M_writer('" alt="">\r\n    </div>\r\n\t<table id="manage_table" class = "table table-striped table-bordered table-hover">\r\n\t\t    <tr>\r\n\t\t      <th>Description</th>\r\n\t\t      <th>Category</th>\r\n\t\t      <th>Current Price</th>\r\n      \t  <th>Producer Name</th>\r\n          <th>Actions</th>\r\n\t\t    </tr>\r\n\t\t\t  <tr>\r\n          <td> ')
        __M_writer(str( product.description ))
        __M_writer(' </td>\r\n          <td> ')
        __M_writer(str( product.category ))
        __M_writer(' </td>\r\n\t\t      <td> $')
        __M_writer(str( product.current_price ))
        __M_writer(' </td>\r\n          <td> ')
        __M_writer(str( product.producer_name ))
        __M_writer(' </td>\r\n          <td width="20%" nowrap>\r\n            <div class="row">\r\n              <div class="col-lg-12">\r\n                <div class="input-group">\r\n                  <input id="quantity_')
        __M_writer(str( product.id))
        __M_writer('" type="text" class="form-control" placeholder="Qty">\r\n                  <span class="input-group-btn">\r\n                    <button id="product_')
        __M_writer(str( product.id))
        __M_writer('" data-pid="')
        __M_writer(str( product.id))
        __M_writer('" class="btn btn-warning" type="button">Add to Cart</button>\r\n                  </span>\r\n                </div><!-- /input-group -->\r\n              </div><!-- /.col-lg-6 -->\r\n            </div><!-- /.row -->\r\n            </td>\r\n\t\t\t    </tr>\r\n\t\t</table>\r\n')
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
        __M_writer('\r\n    <title>CHF: Product Detail</title>\r\n  ')
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
{"line_map": {"66": 48, "115": 30, "133": 47, "71": 51, "145": 3, "139": 3, "175": 169, "157": 53, "81": 50, "110": 28, "87": 50, "120": 37, "27": 0, "93": 10, "163": 7, "101": 10, "102": 12, "103": 12, "104": 16, "105": 16, "106": 16, "107": 16, "108": 27, "109": 27, "46": 1, "111": 28, "112": 29, "113": 29, "114": 30, "51": 5, "116": 35, "117": 35, "118": 37, "119": 37, "56": 8, "121": 37, "151": 53, "61": 45, "169": 7, "127": 47}, "filename": "C:\\Users\\benwillard17\\Documents\\GitHub\\Sprint3\\test_dmp\\homepage\\templates/productlist.viewproduct.html", "source_encoding": "ascii", "uri": "productlist.viewproduct.html"}
__M_END_METADATA
"""
