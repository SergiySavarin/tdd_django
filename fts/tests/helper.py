"""For diferend needed operations"""
import re

def ignore_token(content):
    """ Using for ignoring csrf_token if it's in your html doc.
        example:
        <input name="item_text" id="id_new_item" placeholder="Enter
        a to-do item" value="{{ csrf_token }}" />
        
        Args:
        conntent: string
            html-like string

        Output:
        conntent: string
            html-like string with replaced value=""
    """
    csrf_regex = r'<input[^>]+csrfmiddlewaretoken[^>]+>'
    return re.sub(csrf_regex, '', content)