"""
Copyright 2015 EMC Corporation
All Rights Reserved
EMC Confidential: Restricted Internal Distribution
81ff427ffd0a66013a8e07b7b967d6d6b5f06b1b.ViPR
"""

class CLIInputs:

    wadl_context = dict()
    xsd_elements_dict = dict()
    unknown_xsd_elements_dict = dict()
    name_type_dict = dict()

class ActionParams:

    def __init__(self):
        self.query_params = dict()
        self.method_name = None

class XSDElement:

    def __init__(self, name=None, type=None, min_occurs='0', max_occurs='1', base=None, ref=None):
        self.name = name
        self.type = type
        self.min_occurs = min_occurs
        self.max_occurs = max_occurs
        self.base = base
        self.ref = ref
        self.children = list()
        self.query_params = list()

    def __str__(self):
        return 'name: %s type: %s base: %s ref: %s children: %s' %(self.name, self.type, self.base, self.ref, self.children)

    def __repr__(self):
        return 'name: %s type: %s base: %s ref: %s children: %s' %(self.name, self.type, self.base, self.ref, self.children)

class ChildXSDElement:


    def __init__(self, name=None, type=None, min_occurs=0, max_occurs=1, base=None, ref=None):
        self.name = name
        self.type = type
        self.min_occurs = min_occurs
        self.max_occurs = max_occurs
        self.base = base
        self.ref = ref
        self.children = None

    def __str__(self):
        return 'name: %s type: %s base: %s ref: %s' %(self.name, self.type, self.base, self.ref)

    def __repr__(self):
        return 'name: %s type: %s base: %s ref: %s' %(self.name, self.type, self.base, self.ref)

