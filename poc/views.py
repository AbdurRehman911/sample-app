from django.http import JsonResponse
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import CustomAppUser, Course
from .serializers import CourseSerializer

@csrf_exempt
@api_view(['POST'])
def create_user(request):
    if request.method == 'POST':
        data = request.data
        try:
            user = get_user_model().objects.create_user(email=data['email'], first_name=data['first_name'],
                                                        last_name=data['last_name'],
                                                        username=data['username'],)
            return JsonResponse({'message': 'User created successfully'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
        

@api_view(['POST'])
@permission_classes([AllowAny])
def generate_jwt_token(request):
    if request.method == 'POST':
        # Assuming you have a custom user model named CustomAppUser
        username = request.data.get('username')
        password = request.data.get('password')

        user = CustomAppUser.objects.get(username=username)
        # Generate a refresh token
        refresh = RefreshToken.for_user(user)
        # Return the access token as a JSON response
        return Response({
            'access_token': str(refresh.access_token),
            'refresh_token': str(refresh),
            'expires_at': refresh.access_token['exp'],
        })


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def protected_endpoint(request):
    user = request.user
    return JsonResponse({'message': f'Hello, {user.username}! This is a protected endpoint.'})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def details(request):
    courses = Course.objects.all()
    courses_data = CourseSerializer(courses, many=True).data
    response_data = {"courses": courses_data}
    return Response(response_data)


@api_view(['POST'])
def create_course(request):
    serializer = CourseSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)