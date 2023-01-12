#%%
#!/home/romainm13/rst/srt_venv/bin python
# -*- coding:utf-8 -*-

from flask import Flask, request, render_template

#import whisper code to convert mp3 to srt

#######################
#######################
app = Flask(__name__)
#app.debug = True
# app.secret_key = '2d9-E2.)f&é,A$p@fpa+zSU03êû9_'

@app.route('/')
def upload_form():
    return render_template('index.html')

@app.route("/your-backend-endpoint", methods=["POST"])
def convert_to_srt():
    file = request.files["file"]
    # print("The file is:", file)
    # print("The file name is:", file.filename)
    # print("The file type is:", file.content_type)
    # print("The file size is:", file.content_length)
    # print("The file is:", file.read())
    # print("The file is:", file.stream)
    if file and file.filename.endswith(".mp3"):
        # Use the file object to perform your conversion to SRT here
        pass
    else:
        return "Invalid file type. Please upload an mp3 file."
    return "File converted to SRT successfully!" + " " + file.filename

if __name__ == "__main__":
    app.run(debug=True)

if __name__ == '__main__':
    app.run(debug=True)