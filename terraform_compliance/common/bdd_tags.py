from terraform_compliance.common.defaults import Defaults
from terraform_compliance.common.helper import Match


def look_for_bdd_tags(_step_obj):
    _step_obj.context.no_failure = False
    _step_obj.context.failure_class = None

    if hasattr(_step_obj, 'all_tags') and len(_step_obj.all_tags) > 0:
        _step_obj.context.case_insensitivity = True

        for tag in _step_obj.all_tags:
            if tag.name.lower() in Defaults().no_failure_tags:
                _step_obj.context.no_failure = True
                _step_obj.context.failure_class = tag.name
            elif tag.name.lower() in Defaults().case_sensitive_tags:
                _step_obj.context.case_insensitivity = False

    ## set the match here
    case_sensitive = True if hasattr(_step_obj.context, 'case_insensitivity') and not _step_obj.context.case_insensitivity else False
    _step_obj.context.match = Match(case_sensitive=case_sensitive)

    return _step_obj
