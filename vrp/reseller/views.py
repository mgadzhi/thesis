# -*- coding: utf-8 -*-


def reseller_info(request, id):
    errors = []
    if not request.user.is_reseller:
        errors.append('')