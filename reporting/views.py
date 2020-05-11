from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import User
from .serializers import UserSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
# Create your views here.
@api_view(["POST"])
def registration_view(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data['response'] = "Successfully registered new user."
            data['email'] = user.email
            data['username'] = user.username
        else:
            data = serializer.errors
        return Response(data)

@api_view(["POST"])
def login_view(request):
    if request.method == 'POST':
        serializer = UserLoginSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data['response'] = "Successfully logged in."            
        else:
            data = serializer.errors
        return Response(data)        
@api_view(["POST"])
def savesite(request):
    if request.method == 'POST':
        serializer = SiteSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            site = serializer.save()
            data['response'] = "Successfully saved site data."
            data['siteId']=site.siteId
            data['siteName']=site.siteName
            data['siteLocation']=site.siteLocation
            data['siteInfo']=site.siteInfo
        else:
            data = serializer.errors
        return Response(data)
@api_view(["GET"])
def get_sites(request):
    if request.method == 'GET':
        sites = Site.objects.filter()
        serializer = SiteSerializer(sites, many=true)        
        return JsonResponse({'sites': serializer.data}, safe=False, status=status.HTTP_200_OK)    
@api_view(["PUT"])
def update_site(request, siteId):
    if request.method == 'PUT':
        site = request.siteId
        payload = json.loads(request.body)
        try:
            site_item = Site.objects.filter(siteId=site)
            site_item.update(**payload)
            site = Site.objects.get(siteId=site)
            serializer =  SiteSerializer(site)
            return JsonResponse({'site': serializer.data},safe=False, status=status.HTTP_200_OK)
        except ObjectDoesNotExist as e:
            return JsonResponse({'error': str(e)},safe=False, status=HTTP_404_NOT_FOUND)
        except Exception:
            return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
        
@api_view(["DEL"])
def delete_site(request):
    if request.method == 'POST':
        site = request.siteId
    try:
        site_item = Site.objects.get(siteId=site)
        site_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(data)    
@api_view(["GET"])
def get_site(request):
    if request.method == 'GET':
        site = request.siteId
    try:
        site_item = Site.objects.get(siteId=site)
        serializer =  SiteSerializer(site_item)
        return JsonResponse({'site': serializer.data},safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(data)    
#############Site Activity CRUD###########
@api_view(["GET"])
#@csrf_exempt
#@permission_classes([IsAuthenticated])
def get_siteActivities(request):
    siteActivity = request.siteActivityId
    activities = SiteActivity.objects.filter(siteActivityId=siteActivity)
    serializer = SiteActivitySerializer(activities, many=True)
    return JsonResponse({'activities': serializer.data}, safe=False, status=status.HTTP_200_OK)
@api_view(["POST"])
#@csrf_exempt
#@permission_classes([IsAuthenticated])
def add_siteActivity(request):
    payload = json.loads(request.body)
    siteActivity = request.siteActivityId
    
    try:
      #  site = Site.objects.get(siteActivityId=siteActivity)
        siteActivity = SiteActivity.objects.create(
            ActivityName=payload["activityName"],
            ActivityInfo=payload["ActivityInfo"],
            siteId=payload["siteId"],
            
        )
        serializer = SiteActivitySerializer(siteActivity)
        return JsonResponse({'siteActivity': serializer.data}, safe=False, status=status.HTTP_201_CREATED)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
@api_view(["PUT"])
#@csrf_exempt
#@permission_classes([IsAuthenticated])
def update_siteActivity(request, siteActivityid):
    siteActivity = request.siteActivityId
    payload = json.loads(request.body)
    try:
        siteActivity = SiteActivity.objects.filter(siteId=siteid, siteActivityId=siteActivity)
        # returns 1 or 0
        siteActivity.update(**payload)
        siteActivities = SiteActivity.objects.get(siteActivityId=siteActivity)
        serializer = SiteActivitySerializer()
        return JsonResponse({'siteActivity': serializer.data}, safe=False, status=status.HTTP_201_CREATED)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
@api_view(["DELETE"])
#@csrf_exempt
#@permission_classes([IsAuthenticated])
def delete_siteActivity(request, siteActivityid):
    siteActivity = request.siteActivityId
    try:
        siteActivity = SiteActivity.objects.get(siteId=siteid, siteActivityId=siteactivity)
        siteActivity.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
def get_siteActivity(request,siteActivityid):
    if request.method == 'GET':
        siteActivity = request.siteActivityId
    try:
        siteActivity = SiteActivity.objects.get(siteId=siteid, siteActivityId=siteActivity)
        serializer =  SiteSerializer(siteActivity)
        return JsonResponse({'site': serializer.data},safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(data)    
#############SiteActivityTypeCrud
@api_view(["GET"])
#@csrf_exempt
#@permission_classes([IsAuthenticated])
def get_siteActivityType(request):
    siteactivitytypeid = request.siteActivityTypeId
    activityTypes = SiteActivity.objects.filter(siteActivityTypeId=siteactivitytypeid)
    serializer = SiteActivitySerializer(activityTypes, many=True)
    return JsonResponse({'siteActivityTypes': serializer.data}, safe=False, status=status.HTTP_200_OK)
@api_view(["POST"])
#@csrf_exempt
#@permission_classes([IsAuthenticated])
def add_siteActivityType(request):
    payload = json.loads(request.body)
    siteactivitytypeid = request.siteActivityTypeId
   # activityTypes = SiteActivity.objects.filter(siteActivityTypeId=siteactivitytypeid)
    try:
        site = Site.objects.get(siteActivityTypeId=siteactivitytypeid)
        siteActivity = SiteActivity.objects.create(
            activityTypeInfo=payload["activityTypeInfo"],
            siteActivityid=payload["siteActivityid"],
            reportingFields=payload["reportingFields"],
        )
        serializer = SiteActivityTypeSerializer(siteActivity)
        return JsonResponse({'siteActivity': serializer.data}, safe=False, status=status.HTTP_201_CREATED)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
@api_view(["PUT"])
#@csrf_exempt
#@permission_classes([IsAuthenticated])
def update_siteActivityType(request, siteActivityTypeId):
    siteid = request.siteId
    payload = json.loads(request.body)
    try:
        siteActivityType = SiteActivity.objects.filter(siteId=siteid, siteActivityTypeId=siteActivityTypeId)
        # returns 1 or 0
        siteActivity.update(**payload)
        siteActivity = siteActivityType.objects.get(id=siteActivityTypeId)
        serializer = SiteActivitySerializer(siteActivity)
        return JsonResponse({'siteActivity': serializer.data}, safe=False, status=status.HTTP_201_CREATED)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
@api_view(["DELETE"])
#@csrf_exempt
#@permission_classes([IsAuthenticated])
def delete_siteActivityType(request, siteActivityTypeId):
    siteid = request.siteId
    try:
        siteActivityType = SiteActivity.objects.filter(siteId=siteid, siteActivityTypeId=siteActivityTypeId)
        siteActivity.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
def get_site(request,siteActivityTypeid):
    if request.method == 'GET':
        user = request.siteActivityTypeId
    try:
        siteActivityType = SiteActivity.objects.get(siteId=siteid, id=siteactivityTypeId)
        serializer =  SiteSerializer(siteActivityType)
        return JsonResponse({'site': serializer.data},safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(data)    
####CRUD Reporting

def get_reports(request):
    siteId = request.siteId
    siteActivityId = request.siteActivityId
    
    #userID = request.userID -- change the model to username or user foreign key
    
    reports = Report.objects.filter(siteId=siteId, siteActivityId=siteActivityId)
    serializer = ReportSerializer(activities, many=True)
    return JsonResponse({'reports': serializer.data}, safe=False, status=status.HTTP_200_OK)
@api_view(["PUT"])
#@csrf_exempt
#@permission_classes([IsAuthenticated])
def update_report(request, siteActivityid):
    siteid = request.siteId
    payload = json.loads(request.body)
    try:
        report = Report.objects.filter(siteId=siteid, id=siteactivityid)
        # returns 1 or 0
        #userID
        #siteID
        #ActivityID
        ##ActivityTypeID
        report.update(**payload)
        report = Report.objects.get(siteId=siteid, id=siteactivityid)
        serializer = ReportSerializer()
        return JsonResponse({'Report': serializer.data}, safe=False, status=status.HTTP_201_CREATED)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
@api_view(["DELETE"])
#@csrf_exempt
#@permission_classes([IsAuthenticated])
def delete_report(request, siteActivityid):
    siteid = request.siteId
    try:
        report = Report.objects.get(siteId=siteid, id=siteactivityid)
        report.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
def get_reportbyId(request,reportId):
    if request.method == 'GET':
        user = request.siteActivityid
    try:
        report = Report.objects.get(siteId=siteid, id=siteactivityid)
        serializer =  ReportSerializer(report)
        return JsonResponse({'Report': serializer.data},safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(data)    


####CRUD Profile    
    
    
