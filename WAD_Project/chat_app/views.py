from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Message_Data
from django.forms.models import model_to_dict
from django.contrib.auth.models import User


class get_chat():
    def with_user(request, username):
        # returns a list of messages between request.user and user.username as list of dict
        to_user_id = User.objects.filter(username=username).get()
        from_user_id = request.user.id
        messages = Message_Data.objects.filter(from_user__in=[from_user_id,to_user_id], to_user__in=[from_user_id, to_user_id])
        ret = list()
        for each in messages:
            ret.append({
                "msg":each.msg,
                "time":each.datetime_stamp,
                "sent":each.from_user.pk==from_user_id
            })
        # return messages
        return ret

    def between_users(request, username):
        # returns a list of messages between request.user and user.username
        to_user_id = User.objects.filter(username=username).get()
        from_user_id = request.user.id
        messages = Message_Data.objects.filter(from_user__in=[from_user_id,to_user_id], to_user__in=[from_user_id, to_user_id])
        return messages

        
    def getAllMsgDict(username):
        print("getAllMsg.username = ",username)
        user = User.objects.filter(username=username).get()
        sent = Message_Data.objects.filter(from_user=user)
        recv = Message_Data.objects.filter(to_user=user)
        ret = list()
        for each in sent:
            ret.append({
                "msg":each.msg,
                "time":each.datetime_stamp,
                "sent":True
            })
        for each in recv:
            ret.append({
                "msg":each.msg,
                "time":each.datetime_stamp,
                "sent":False
            })
        # all = sent.union(recv)
        # return list(all)
        return ret
    
    def getAllMsg(username):
        user = User.objects.filter(username=username).get()
        sent = Message_Data.objects.filter(from_user=user)
        recv = Message_Data.objects.filter(to_user=user)
        all = sent.union(recv)
        return list(all)

    def friend_id(all_messages):
        s = set()
        for each_msg in all_messages:
            s.add(each_msg.from_user.id)
            s.add(each_msg.to_user.id)
        return list(s)

    def mini_chat(request,all_msg, friend_ids):
        # Returns a list of dictionary
        # dictionary := name, msg_time, msg
        # required data : all messages between request user and his contacts
        ret = list()
        for each_id in friend_ids:
            d = dict()
            u = User.objects.filter(id=each_id).get()
            messages = get_chat.between_users(request,u.username)
            print("messages : ", messages)
            messages = messages.order_by('datetime_stamp')
            messages = list(messages)
            print("messages : ", messages)
            if(len(messages)==0):
                continue
            m = messages[-1]
            d["name"] = u.username
            d["msg_time"] = m.getTimeIST
            d["msg"] = m.msg
            print("min chat function d : ", d)
            ret.append(d)
        return ret


   

# Create your views here.
def chat(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect('signinviarec')

    username = kwargs.get("un")
    with_user = User.objects.filter(username=username).get()

    # recreate mini-chat data form complete data
    d = {
        "mini_chat_data":list(),
        "message":list(),
        "focused_name": with_user,
    }

    conversation = get_chat.with_user(request, username)
    all_msg = get_chat.getAllMsg(request.user.username)
    # conversation.order_by('datetime_stamp')
    conversation.sort(key=lambda x: x["time"])
    d["message"] = list(conversation)


    friend_id = get_chat.friend_id(all_msg)
    d["mini_chat_data"] = get_chat.mini_chat(request, all_msg, friend_id)
    print("min chat data : ")
    pretty(d)

    if request.method=="POST":
        print("\n\n\got a POST, values : ",request.POST["message_field"],"\n\n")
        current_user = request.user
        print(current_user.id,current_user)
        msg = Message_Data()
        msg.from_user = request.user
        msg.to_user = with_user
        msg.msg = request.POST["message_field"]
        if valid(msg):
            msg.save()
    
    return render(request,"chat.html",d)




def chatAll(request):
    if not request.user.is_authenticated:
        return redirect('signinviarec')

    # Create mini-chat data form complete data
    d = {
        "mini_chat_data":list(),
        "message":list(),
        "focused_name": None,
    }

    all_msg = get_chat.getAllMsg(request.user.username)
    friend_id = get_chat.friend_id(all_msg)
    d["mini_chat_data"] = get_chat.mini_chat(request, all_msg, friend_id)

    return render(request,"chat.html",d)


# utility functions
def valid(msg):
    if msg.msg == '':
        return False

def pretty(d, indent=0):
   for key, value in d.items():
      print('\t' * indent + str(key))
      if isinstance(value, dict):
         pretty(value, indent+1)
      else:
         print('\t' * (indent+1) + str(value))
