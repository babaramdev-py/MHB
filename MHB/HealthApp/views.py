from django.shortcuts import render
from django.views.generic import CreateView
from HealthApp import forms
from time import sleep
import openai
openai.api_key = "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"
messages = [{"role": "system", "content": "You are an empathetic friend that listens and provides guidance only, you respond to no other questions other than emotional ones."}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply


    
def AIView(request):
    if request.method == "POST":
        chat_form = forms.InputForm(request.POST)

        if chat_form.is_valid():
            param = chat_form.cleaned_data['text']
            print(param)
            response = CustomChatGPT(param)
            print(response)
        return render(request,'ai.html',{'response':response,'form':forms.InputForm})
        
        
        # render(request,'ai.html',{'response':response})
    else:
        return render(request,'ai.html',{'form':forms.InputForm})

