from flask import Blueprint, render_template, request, flash, redirect

contact_bp = Blueprint('contact', __name__)

@contact_bp.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Save or process message here
        flash("Message sent successfully!")
        return redirect('/contact')
    return render_template('contact.html')
