from django.conf.urls import url

from . import views

app_name = 'backoffice'
urlpatterns = [
    url('^login/$', views.LoginView.as_view(), name='login'),
    url('^logout/$', views.logout_view, name='logout'),
    url('^switch-user/$', views.switch_user, name='switch-user'),

    url('^create_user/$', views.create_user_view, name='create-user'),
    url('^users/reset_password/(?P<pk>[0-9]+)/$', views.ResetPasswordView.as_view(), name='reset-password'),
    url('^users/$', views.UserListView.as_view(), name='user-list'),

    url('^session/new/$', views.new_session, name='new-session'),
    url('^session/(?P<pk>[0-9]+)/end/$', views.end_session, name='end-session'),
    url('^session/(?P<pk>[0-9]+)/report/$', views.session_report, name='session-report'),
    url('^session/(?P<pk>[0-9]+)/resupply/$', views.resupply_session, name='resupply-session'),
    url('^session/(?P<pk>[0-9]+)/move/$', views.move_session, name='move-session'),
    url('^session/(?P<pk>[0-9]+)/reverse/$', views.reverse_session_view, name='reverse-session'),
    url('^session/(?P<pk>[0-9]+)/$', views.SessionDetailView.as_view(), name='session-detail'),
    url('^session/$', views.SessionListView.as_view(), name='session-list'),
    url('^reports/$', views.ReportListView.as_view(), name='report-list'),

    # These are called 'wizard' cause they're only for wizards (erm, superusers)
    url('^wizard/users/$', views.WizardUsersView.as_view(), name='wizard-users'),
    url('^wizard/settings/$', views.WizardSettingsView.as_view(), name='wizard-settings'),
    url('^wizard/cashdesks/$', views.WizardCashdesksView.as_view(), name='wizard-cashdesks'),
    url('^wizard/import/$', views.WizardPretixImportView.as_view(), name='wizard-import'),
    url('^wizard/items/$', views.WizardItemListView.as_view(), name='wizard-items-list'),
    url('^wizard/items/new$', views.WizardItemCreateView.as_view(), name='wizard-items-create'),
    url('^wizard/items/(?P<pk>[0-9]+)/$', views.WizardItemEditView.as_view(), name='wizard-items-edit'),

    url('^$', views.MainView.as_view(), name='main'),
]
