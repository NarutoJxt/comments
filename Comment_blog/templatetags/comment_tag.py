from django import template
register = template.Library()
@register.filter(name="judge_empty")
def judge_empty(comment_dict,comment):
    if len(comment_dict[comment]) > 0:
        return True
    else:
        return False
@register.inclusion_tag("comment_tree.html")
def get_comment_tree(comment,comment_dict):
    comments = comment_dict[comment]
    return {
        "comments":comments,
        "comment_dict":comment_dict
    }
