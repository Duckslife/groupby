# -*- coding: utf-8 -*-
#
# created by Kim

import json

import yaml

import models

import os
_appcfg = None


def load_appcfg():
    global _appcfg
    connection_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), './connection.yaml')
    with open(connection_path) as fp:
        opt = yaml.load(fp)
        _appcfg = models.AppConfig.from_json(json.dumps(opt))
    return _appcfg


def is_local_stage():
    global _appcfg
    return _appcfg.application.stage == "local"


def is_production_stage():
    global _appcfg
    return _appcfg.application.stage == "production"
