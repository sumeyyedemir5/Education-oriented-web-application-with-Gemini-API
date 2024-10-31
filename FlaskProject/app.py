from flask import Flask, render_template, request, jsonify
import requests
import google.generativeai as genai
import os

app = Flask(__name__)

# API anahtarını Python ortam değişkeni olarak tanımlayın
os.environ["API_KEY"] = "AIzaSyAzEWGbK88p5p4tjRevEqNsYPhUPgmFlaU"

# GenAI modülünü API anahtarıyla yapılandırın
genai.configure(api_key=os.environ["API_KEY"])
model = genai.GenerativeModel('gemini-pro')

def get_response_from_gemini(prompt):
    response = model.generate_content(prompt)
    return response.text if response else "Hata oluştu."

# Ana sayfa rotası
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/page1')
def page1():
    return render_template('page1.html')

@app.route('/page2')
def page2():
    return render_template('page2.html')

@app.route('/page3') 
def page3(): 
    return render_template('page3.html')

@app.route('/page4') 
def page4(): 
    return render_template('page4.html')

# Bilgi alma rotası (AJAX ile)
@app.route('/get_info', methods=['POST'])
def get_info():
    subject = request.form['subject']
    prompt = f"{subject} konusunu detaylı şekilde başlıklar halinde ve örneklerle açıkla."
    result = get_response_from_gemini(prompt)
    return jsonify(result=result)

@app.route('/get_study_schedule', methods=['POST']) 
def get_study_schedule(): 
    prompt = request.form['prompt'] 
    result = get_response_from_gemini(prompt) 
    return jsonify(result=result)

if __name__ == '__main__':
    app.run(debug=True)
