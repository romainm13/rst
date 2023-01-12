#%%
#!/home/romainm13/rst/srt_venv/bin python
# -*- coding:utf-8 -*-

from flask import Flask, request

app = Flask(__name__)
#app.debug = True
app.secret_key = '2d9-E2.)f&é,A$p@fpa+zSU03êû9_'

#########################
## AUXILIARY FUNCTIONS ##
#########################
def process_mp3(mp3_file):
    # TODO: Write code to process the MP3 file and generate the SRT file
    return srt_file
#########################
#########################

@app.route('/')
def upload_form():
    return '''
    <form method="POST" enctype="multipart/form-data">
        <input type="file" name="mp3_file">
        <input type="submit" value="Start">
    </form>
    '''

@app.route('/', methods=['POST'])
def upload_file():
    # Get the uploaded file
    mp3_file = request.files['mp3_file']
    
    # Process the MP3 file and generate the SRT file
    srt_file = process_mp3(mp3_file)
    
    # Create a response to send the SRT file to the client
    response = make_response(srt_file)
    response.headers["Content-Disposition"] = "attachment; filename=output.srt"
    return response

if __name__ == '__main__':
    app.run(debug=True)