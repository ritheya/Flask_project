from flask import Flask,render_template,request,redirect,url_for
import os
import re
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
          sentence_count = len(re.findall(r'[.!?]', content))
          para=len([p for p in content.split('\n\n') if p.strip()])
          avg_word=(sum([len(w) for w in word])/count) if count>0 else 0
          words=content.lower().split()
          word_freq={}
          for word in words:
              if word in word_freq:
                  word_freq[word]+=1
              else:
                  word_freq[word]=1
          most_freq=[]
          highest=max(word_freq.values())
          for word ,freq in word_freq.items():
              if freq==highest:
                 most_freq.append(word)            
          return render_template('result.html', count=count,char=char_count,sent_count=sentence_count,para_c=para,av=avg_word,most=most_freq)
if __name__=='__main__':
    port=int(os.environ.get("PORT",5000))
    app.run(debug=True,host='0.0.0.0',port=port)