from flask import Flask, render_template, request,redirect
app = Flask(__name__)


@app.route('/',methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
      print('submitted')
      user_name = request.form.get('user_Name')
      visit_date = request.form.get('Visit')
      mr_delay = request.form.get('MR Delay')
      mf = request.form.get('Male/Female')
      hand = request.form.get('Right/Left')
      age = request.form.get('Age')
      educ = request.form.get('educ') 
      ses = request.form.get('SES')
      mmse = request.form.get('MMSE') 
      cdr = request.form.get('CDR')
      etiv = request.form.get('eTIV')
      nwbv = request.form.get('nWBV')
      asf = request.form.get('ASF')
      data = [user_name,visit_date,mr_delay,mf,
              hand,age,educ,ses,mmse,cdr,etiv,nwbv,asf]
      print(data)
      redirect('/result')
    return render_template('form.html')

@app.route('/result', methods=['GET', 'POST'])
def result():
    return render_template('result.html')


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8000, debug=True)
