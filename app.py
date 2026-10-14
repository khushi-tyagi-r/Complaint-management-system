from flask import Flask
app = Flask(__name__)
complaints=[]

@app.route('/')
def home():
    html="<h2>Complaint System</h2><form action='/add' method='post'>Name:<br><input name='name'><br>Complaint:<br><textarea name='msg'></textarea><br><button>Submit</button></form><br><a href='/view'>View Complaints</a><br><br>".replace("<br>","\n")
    for c in complaints:
        html+=f"<p><b>{c[0]}</b>: {c[1]}</p>"
    return html

@app.route('/add', methods=['POST'])
def add():
    from flask import request
    complaints.append((request.form['name'], request.form['msg']))
    return "<h3>Submitted!</h3><a href='/'>Back</a> | <a href='/view'>View</a>"

@app.route('/view')
def view():
    s="<h2>All Complaints</h2>"
    if not complaints:
        s+="<p>No complaints</p>"
    for i,c in enumerate(complaints):
        s+=f"<p>{i+1}. {c[0]} - {c[1]}</p>"
    s+="<br><a href='/'>Home</a>"
    return s

if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000)
