import os
from flask import Blueprint, render_template, request, redirect, url_for, flash, session

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

ADMIN_USER = "admin"
ADMIN_PASSWORD = "test123"
'''
ADMIN_USER = os.getenv('ADMIN_USER', 'admin')
ADMIN_PASSWORD = os.getenv('ADMIN_PASSWORD', 'changeme')
'''

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '')
        if username == ADMIN_USER and password == ADMIN_PASSWORD:
            session['role'] = 'admin'
            flash('Logged in as admin', 'success')
        else:
            #other customers
            session['role'] = 'user'
            flash('Logged in', 'success')
        return redirect(request.args.get('next') or url_for('product.display_products_page'))
    return render_template('login.html')

@auth_bp.route('/logout')
def logout():
    session.pop('role', None)
    flash('Logged out', 'info')
    return redirect(url_for('product.display_products_page'))
