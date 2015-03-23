# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425788416.013869
_enable_loop = True
_template_filename = 'C:\\Users\\benwillard17\\test_dmp\\homepage\\templates/index.html'
_template_uri = 'index.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['jumbotron', 'content_left', 'content_right', 'content', 'content_center']


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
        def content_right():
            return render_content_right(context._locals(__M_locals))
        def jumbotron():
            return render_jumbotron(context._locals(__M_locals))
        def content_left():
            return render_content_left(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        def content_center():
            return render_content_center(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'jumbotron'):
            context['self'].jumbotron(**pageargs)
        

        __M_writer('\r\n\r\n<div padding-bottom: 25px;>\r\n')
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
        __M_writer('\r\n    \r\n            <div class="jumbotron">\r\n              \r\n              <div class="image">\r\n                <img src="/static/homepage/media/autumn-in-park.jpg">\r\n              </div>\r\n              <p class="quote">Quote of the day <br> <q>Three millions of people, armed in the holy cause of liberty, and in such a country as that which we possess, are invincible by any force which our enemy can send against us. Beside, sir, we shall not fight our battles alone.<br> There is a just God who presides over the destinies of Nations, and who will raise up friends to fight our battles for us.</q><br> -- Patrick Henry</p>\r\n              <h1>Welcome to the Colonial Heritage Foundation!</h1>\r\n              <br>\r\n                \r\n              <div class="row">\r\n                <div class="col-md-4">\r\n                <h2>Learn</h2>\r\n                  <p>Colonial History <br> Fun Facts <br>\r\n                    Enthralling Culture <br>\r\n                  and Your Heritage <br>\r\n                  </p>\r\n                </div>\r\n                <div class="col-md-4">\r\n                <h2>Discover</h2>\r\n                  <p>Discover a world of adventure. <br>\r\n                Log in or become \r\n                a member <br> for full \r\n                access to the site, <br>\r\n                including ordering and  renting <br> real colonial artifacts!<br></p>\r\n                </div>\r\n                <div class="col-md-4">\r\n                  <h2>Explore</h2>\r\n                  <p>Events <br> Areas <br>\r\n                  Products <br>\r\n                  ..and more! <br></p>\r\n                </div>\r\n                </div>\r\n                </div>\r\n              </div>\r\n        </div>\r\n\r\n            <!--<h1>Content</h1>\r\n            <p>\r\n              This is the text that will fill up the homepage. We will be writing this later. This text will be different on every page because I am using the block element which will take the content on the other pages, and replace it on this base page. I am writing to fill up space.<br><br>\r\n              \r\n              Now I am writing another paragraph to make the length of the column bigger. I am still trying to find out how to make it change the height dynamically.<br><br> \r\n            </p>\r\n           \r\n            <span class="label label-warning">Do you accept the terms? (label)<span class="glyphicon glyphicon-exclamation-sign" aria-hidden="true"></span></span>\r\n            <button type="button" class="btn btn-success">Success</button>\r\n            <button type="button" class="btn btn-primary">Primary</button>-->\r\n        </div>\r\n      </div><!-- row -->\r\n    </div><!-- container -->\r\n')
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
{"uri": "index.html", "source_encoding": "ascii", "line_map": {"96": 66, "132": 126, "102": 66, "72": 3, "42": 1, "108": 7, "78": 3, "47": 4, "114": 7, "84": 60, "126": 63, "57": 61, "120": 63, "52": 58, "90": 60, "27": 0, "62": 64}, "filename": "C:\\Users\\benwillard17\\test_dmp\\homepage\\templates/index.html"}
__M_END_METADATA
"""
