# -*- coding:utf-8 -*-


from .. import db
from . import show
from flask import render_template, abort, redirect, request, current_app, url_for, flash, json, jsonify, send_from_directory


@show.route('/', methods = ['GET', 'POST'])
@show.route('/index', methods = ['GET', 'POST'])
def index():

    return render_template('show/index.html')


