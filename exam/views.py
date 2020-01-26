from django.shortcuts import render , redirect
from .models          import Questions , Chosen, Users
import json  ;        import random
from django.views     import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView
from django.contrib.auth  import authenticate , login , get_user_model
from django.contrib.auth.hashers import check_password, make_password
# Create your views here.


# ===================================   main page get 20 question =====================
def Main(request):

    if request.method == "GET":
        ids_pack = []  ; rand_pack = []
        chosen = []

        # delete Chosen model attributes
        chosen = Chosen.objects.all().delete()
        # create a random id list from question ids
        ids_quest = Questions.objects.all().values('id')
        for i in ids_quest:
            ids_pack.append(i['id'])
        for i in range(0,10):
            a = random.choice(ids_pack)
            rand_pack.append(a)
            ids_pack.remove(a)

        # get question from Question models with id
        for i in rand_pack:
            end_quest = Questions.objects.filter(id=str(i))
            for j in end_quest:
                ch_id = j.id
                ch_quest = j.questpack
                ch_A = j.A
                ch_B = j.B
                ch_C = j.C
                ch_D = j.D
                ch_truequest = j.truequest

                # add random question in Chosen model
                new = Chosen(id=ch_id, questpack=ch_quest, A= ch_A, B=ch_B, C=ch_C, D=ch_D, truequest=ch_truequest)
                new.save()

        chosen_quest = Chosen.objects.all()


        context = {
                "all_quest": chosen_quest,
                "Error" : "Please Loging"
            }

        return render(request , "Index.html" , context)


# =======================================================================================================================

@csrf_exempt
def Result(request):

    if request.method == "POST":
        
        chosen = Chosen.objects.all()
        score = 0 ; mistake = 0 ; none_choice = 0  ;  true_resp = 0

        for x in chosen:
            
            choise_alter = request.POST.get(str(x.id))
            if choise_alter == 'A':
                x.AB = True
            elif choise_alter == 'B':
                x.BB = True
            elif choise_alter == 'C':
                x.CB = True
            elif choise_alter == 'D':
                x.DB = True
            elif choise_alter == 'none':
                x.none = True
            x.save()
            

        
        for x in chosen:
            Choise_quest = Chosen.objects.get(id=str(x.id))

            none_rsp = Choise_quest.none
            a_rsp = Choise_quest.AB
            b_rsp = Choise_quest.BB
            c_rsp = Choise_quest.CB
            d_rsp = Choise_quest.DB
            n_rsp = Choise_quest.none
            respn = Choise_quest.truequest
            
            # if none is flase find true alternative
            if n_rsp == False:
                result = [a_rsp, b_rsp, c_rsp, d_rsp]

                if result[0] == True:
                    response = "AB"
                elif result[1] == True:
                    response = "BB"
                elif result[2] == True:
                    response = "CB"
                elif result[3] == True:
                    response = "DB"

                # take score if respone is True
                if response == str(respn):
                    score = score + 3
                    true_resp = true_resp + 1
                else:
                    score = score - 1
                    mistake = mistake - 1

            else:
                none_choice = none_choice - 1
                continue

        score = score / 3

        context = {
                'true_resp' :true_resp,
                'mistake' : mistake,
                'none_choice' : none_choice,
                "final_score": score,
                "Error" : "Success"
            }

        return render(request , "Result.html" , context)

    else:
        return render(request , "Result.html")

# =======================================================================================================================
    