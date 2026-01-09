from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate, get_user_model
from django.views.generic import TemplateView
from .models import Tag, DisruptionEntry, RootCauseRule, SuggestionTemplate
from .serializers import UserSerializer, TagSerializer, DisruptionEntrySerializer, RootCauseRuleSerializer, SuggestionTemplateSerializer

User = get_user_model()

class LoginTemplateView(TemplateView):
    template_name = "core/login.html"

class RegisterTemplateView(TemplateView):
    template_name = "core/register.html"

class DashboardTemplateView(TemplateView):
    template_name = "core/dashboard.html"

class LogEntryTemplateView(TemplateView):
    template_name = "core/log_entry.html"

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSerializer

class LoginView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class TagListCreateView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class TagDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class DisruptionEntryListCreateView(generics.ListCreateAPIView):
    serializer_class = DisruptionEntrySerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return DisruptionEntry.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class DisruptionEntryDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DisruptionEntrySerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return DisruptionEntry.objects.filter(user=self.request.user)

class RootCauseRuleListCreateView(generics.ListCreateAPIView):
    queryset = RootCauseRule.objects.all()
    serializer_class = RootCauseRuleSerializer
    permission_classes = (permissions.IsAdminUser,)

class RootCauseRuleDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = RootCauseRule.objects.all()
    serializer_class = RootCauseRuleSerializer
    permission_classes = (permissions.IsAdminUser,)

class SuggestionTemplateListCreateView(generics.ListCreateAPIView):
    queryset = SuggestionTemplate.objects.all()
    serializer_class = SuggestionTemplateSerializer
    permission_classes = (permissions.IsAdminUser,)

class SuggestionTemplateDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SuggestionTemplate.objects.all()
    serializer_class = SuggestionTemplateSerializer
    permission_classes = (permissions.IsAdminUser,)
