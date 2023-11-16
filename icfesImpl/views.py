from pathlib import Path
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import joblib


@csrf_exempt
def indexFunc(request):
    return render(request, 'index.html')

@csrf_exempt
def predecir(request):
    
    if( request.method == 'POST' ): 
 
        #cargar modelo
        ruta= str(Path(__file__, '../', './model/saberpro_coraeran.joblib').resolve())
        print("ruta: ",ruta)

        try:
            print('cargado')
            model = joblib.load( ruta )
        except Exception as err:
            print("Error", err)
        
        #Cagar Body
        body = json.loads(request.body)
        print(body)
        
        #hacer predicción

        try:
            prediccion = model.predict([       
                [
                    body['param1'], body['param2'], body['param3'], body['param4'], body['param5'], body['param6'], body['param7'], body['param8'], body['param9'], body['param10'],
                    body['param11'], body['param12'], body['param13'], body['param14'], body['param15'], body['param16'], body['param17'], body['param18'], body['param19'], body['param20'],
                    body['param21'], body['param22'], body['param23'], body['param24'], body['param25'], body['param26'], body['param27'], body['param28'], body['param29'], body['param30'],
                    body['param31'], body['param32'], body['param33'], body['param34'], body['param35'], body['param36'], body['param37'], body['param38'], body['param39'], body['param40'],
                    body['param41'], body['param42'], body['param43'], body['param44'], body['param45'], body['param46'], body['param47'], body['param48'], body['param49'], body['param50'],
                    body['param51'], body['param52'], body['param53'], body['param54'], body['param55'], body['param56'], body['param57'], body['param58'], body['param59'], body['param60'],
                ]
            ])
            print(f"Predicción: {prediccion[0]}")

            rs = 0
            if(prediccion[0] == True):
                rs=1

            data = {
                'result': rs,
                'values': body 
            }  

            resp = JsonResponse(data, status=200)
            return resp
        except Exception as err:
            print(f"Error: {err}")
        
    else:  
        return JsonResponse({ 'msg': 'Upps hiciste mal la petición' }, status=400)