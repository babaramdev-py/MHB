from django.shortcuts import render
from django.views.generic import CreateView
from HealthApp import forms
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


    
def HomePage(request):
    if request.method == "POST":
        chat_form = forms.InputForm(request.POST)

        if chat_form.is_valid():
            param = chat_form.cleaned_data['text']
            response = CustomChatGPT(param)
            print(response)
        return render(request,'ai.html',{'form':forms.InputForm})
        
        
        # render(request,'ai.html',{'response':response})
    else:
        return render(request,'ai.html',{'form':forms.InputForm})

