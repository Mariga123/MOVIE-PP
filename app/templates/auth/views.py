from flask_login import login_user,logout_user,login_required

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))