from django.shortcuts import render
from django.views.generic import CreateView, TemplateView, ListView
from HealthApp import forms,secrets
from .models import Therapist
import openai
openai.api_key =  secrets.API_KEY
messages = [{"role": "system", "content": "You are a therapist, you only provide guidance on mental health and no other domain strictly."}]

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

class TherapistListView(ListView):
    model = Therapist
    template_name = 'therapist_list.html'
    context_object_name = 'therapists'

    def get_queryset(self):
        return Therapist.objects.all()
