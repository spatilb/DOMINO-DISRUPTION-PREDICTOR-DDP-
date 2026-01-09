from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import (
    RegisterView, LoginView,
    TagListCreateView, TagDetailView,
    DisruptionEntryListCreateView, DisruptionEntryDetailView,
    RootCauseRuleListCreateView, RootCauseRuleDetailView,
    SuggestionTemplateListCreateView, SuggestionTemplateDetailView,
    LoginTemplateView, DashboardTemplateView, LogEntryTemplateView, RegisterTemplateView
)

urlpatterns = [
    # Frontend Pages
    path('', LoginTemplateView.as_view(), name='login_page'),
    path('register/', RegisterTemplateView.as_view(), name='register_page'),
    path('dashboard/', DashboardTemplateView.as_view(), name='dashboard_page'),
    path('log-entry/', LogEntryTemplateView.as_view(), name='log_entry_page'),

    # API Endpoints
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('api/auth/login/', LoginView.as_view(), name='login'),
    path('api/auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('api/tags/', TagListCreateView.as_view(), name='tag-list-create'),
    path('api/tags/<int:pk>/', TagDetailView.as_view(), name='tag-detail'),

    path('api/disruption/', DisruptionEntryListCreateView.as_view(), name='disruption-list-create'),
    path('api/disruption/<int:pk>/', DisruptionEntryDetailView.as_view(), name='disruption-detail'),
    path('api/disruption/user/', DisruptionEntryListCreateView.as_view(), name='user-disruption-list'),

    path('api/root-cause-rules/', RootCauseRuleListCreateView.as_view(), name='root-cause-rule-list-create'),
    path('api/root-cause-rules/<int:pk>/', RootCauseRuleDetailView.as_view(), name='root-cause-rule-detail'),

    path('api/suggestion-templates/', SuggestionTemplateListCreateView.as_view(), name='suggestion-template-list-create'),
    path('api/suggestion-templates/<int:pk>/', SuggestionTemplateDetailView.as_view(), name='suggestion-template-detail'),
]