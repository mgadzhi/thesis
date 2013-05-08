# -*- coding: utf-8 -*-
from tastypie.authorization import Authorization as BaseAuthorization


class Authorization(BaseAuthorization):

    def read_list(self, object_list, bundle):
        actor = bundle.request.user
        return object_list.filter(reseller=actor)