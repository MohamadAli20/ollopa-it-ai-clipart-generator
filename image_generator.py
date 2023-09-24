from flask import Flask, render_template, request, redirect, url_for
import openai
#install flask and openai first via pip on the terminal:
#pip install openai
#pip install flask

#--FLASK FOR LINKING THE HTML FORM TO PYTHON CODE--
# add template folder as an argument
app = Flask (__name__, template_folder='template')

#--MAIN CLIPART GENERATOR VIA OPENAI API KEY--
openai.api_key = "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" #API Key from Shyra's Account user_prompt = "clipart style of a "+p #input prompt or description of desired output

# defines the root route for the application
@app.route('/', methods = ['GET', 'POST'])
def user_input(): # this is called when the root route is accessed

    if request.method == "POST":
        global image_url
        # getting textarea with name = prompt in HTML form
        form_prompt = request.form.get("prompt")
        # getting input with name = no_output in HTML form
        form_no_output = request.form.get("no_output")
        # getting select with name = size
        form_size = request.form.get("size")

        # reassigning the value of form_size
        if form_size == "small":
            form_size = "256x256"
        elif form_size == "medium":
            form_size = "512x512"
        elif form_size == "large":
            form_size = "1024x1024"
        else:
            pass
        
        # passing in the prompt, n and size
        response = openai.Image.create(
            prompt = form_prompt,
            n = int(form_no_output), #parse string / character to integer
            size= form_size
        )

        # url is extracted from response and store in the image_url
        image_url = response['data'][0]['url']
        # print(image_url) # remove this after testing
        
        # Test if this statement returns the selected values get from HTML form and display, remove this after
        # return form_prompt + " " + form_no_output + " " + form_size 
        return render_template('form.html', generated_image_url = image_url)

    return render_template('form.html')

# run the app
if __name__=='__main__':
   app.run(debug=True) #debug=True shows error in the web browser


