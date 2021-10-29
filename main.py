from flask import Flask,render_template,request,flash,redirect,url_for
app = Flask(__name__)

@app.route("/")
def home():
    home = "this is my home page"
    return render_template('index.html', home1= home)
@app.route("/textanalyzer",methods=['GET','POST'])
def textAnalyze():
    text = request.args.get('text')
    wordcount = request.args.get('wordcount',default="off")
    removepunch =  request.args.get('removepunc',default="off")
    uppercase = request.args.get('upper',default="off")
    spaceremove =  request.args.get('spaceremov',default="off")
    newlineemov = request.args.get('newlineemov',default="off")
    if wordcount == "on":
        text = text.split()
        analyzed = len(text)
        params = {'task':'Word Count','analyzed_text':analyzed}
        return render_template('analyze.html',params=params)
        

    elif  removepunch== "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

        for char in text:
            if char in punctuations:
                text = text.replace(char,"")
        analyzed = text
        params = {'task':'Remove punctuations','analyzed_text':analyzed}
        return render_template('analyze.html',params=params)

    elif uppercase=="on":
        analyzed = ""
        for char in text:
            analyzed = analyzed + char.upper()
        params = {'task':'UpperCase Convert','analyzed_text':analyzed}
        return render_template('analyze.html',params=params)
    elif spaceremove =="on":
        analyzed = ""
        i = 0
        for char in text:
            if not(text[i] ==" " and text[i+1]==" "):
                analyzed = analyzed + char
            i = i +1
        params = {'task':'ExtraSpace Remove','analyzed_text':analyzed}
        return render_template('analyze.html',params=params)
    elif ( newlineemov == "on"):
        analyzed = ""
        for char in text:
            if char != "\n":
                analyzed = analyzed + char
        params = {'task':'New Line Remove','analyzed_text':analyzed}
        return render_template('analyze.html',params=params)
    
    else:
         flash('Error Please Select One item')
         return render_template("msg.html")
    
  



if __name__ == "__main__":
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run(debug=True)
