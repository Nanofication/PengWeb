from flask import Blueprint, render_template, request, flash, redirect, url_for
from app.models.product import Product
from app.models import email

footer_bp = Blueprint('footer', __name__)

def email_exists(email_addr):
    existing = email.find_email(email_addr)
    if existing:
        flash('This email is already subscribed!', 'warning')
        return

@footer_bp.route('/subscribe', methods=['POST'])
def subscribe():
    name = request.form.get('name')
    email_addr = request.form.get('email')

    # Check if email exists
    email_exists(email_addr)
    # Save to database
    email.save_user(name, email_addr)

    email.find_email(email_addr)

    return redirect('/')