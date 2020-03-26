from flask import Flask,render_template

@app.route("/admin/dashboard")
def admin_dashboard():
    return render_template("admin/dashboard.html")