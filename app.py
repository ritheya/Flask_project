from flask import Flask,render_template,request,redirect,url_for
import os
app=Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
@app.route('/')
def home():
    techs=['HTML','CSS','FLASK','PYTHON']
    name='Lets explore code'
    return render_template('home.html',techs=techs,name=name,title='Home')
@app.route('/about')
def about():
    name='Lets explore code'
    return render_template('about.html',name=name,title='About')
@app.route('/result')
def result():
    return render_template('result.html')
@app.route('/post', methods=['GET', 'POST'])
def post():
    name='Text Analyzer'
    if request.method=='GET':
       return render_template('post.html',name=name,title='Post')
    if request.method=='POST':
          content = request.form['content']
          word=content.split()
          count=len(word)
          char_count=len(content)
          return render_template('result.html', count=count,char=char_count)
if __name__=='__main__':
    port=int(os.environ.get("PORT",5000))
    app.run(debug=True,host='0.0.0.0',port=port)