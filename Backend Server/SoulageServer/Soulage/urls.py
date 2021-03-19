from django.urls import path, include
from . import views
from rest_framework import routers
from .api_views import UserViewset, OrganisationViewset, DonationViewset, RequestViewset

router = routers.DefaultRouter()
router.register(r"users", UserViewset)
router.register(r"organisations", OrganisationViewset)
router.register(r"donations", DonationViewset)
router.register(r"request", RequestViewset)

urlpatterns = [
    # APIs

    path("", views.index, name="index"),
    path("", include(router.urls)),
    # path("sentiment", views.get_sentiment_API, name="sentiment_api"),
    # path("dump_sentiment", views.dump_sentiment, name="dump_sentiment"),

    # Approve or reject requests
    path("approve_reject_request", views.approve_reject_requests,
         name="approve_reject_request"),

    # Making donations
    path("make_donation", views.make_donation, name="make_donation"),

    # Retrieving topics
    path("get_topics", views.get_topics, name="get_topics"),

    # Get specific donations
    path("get_donations/<str:topic_name>",
         views.get_request_pool, name="get_donations"),

    #     path("get_dashboard_data", views.get_dashboard_data, name="get_dashboard_data"),

    # Websites
    # Admin
    path("admin_login", views.admin_login, name="admin_login"),
    path("render_admin_dashboard", views.render_admin_dashboard,
         name="render_admin_dashboard"),
    path("admin_tables", views.admin_tables, name="admin_tables"),
    path("render_admin_login", views.render_admin_login, name="render_admin_login"),
    path("get_sentiment", views.get_dashboard_data, name="dashboard_data"),
    #     path("admin_test_model", views.model_tester, name="admin_test_model"),

    # VE
    path("render_ve_dashboard", views.render_ve_dashboard,
         name="render_ve_dashboard"),
    path("render_model_evaluator", views.model_tester, name="ve_model_tester"),
    path("request_donation_request", views.ve_request_donation,
         name="ve_request_donation_decision"),
    path("organization_poc_request", views.ve_organization_request,
         name="ve_org_request_decision"),
    path("decision/<int:id>/<int:decision>",
         views.ve_request_decision, name="ve_request_decision"),
    path("poc_decision/<int:id>/<int:decision>",
         views.ve_poc_decision, name="ve_poc_decision"),

    # Organisational POC
    path("render_poc_dashboard", views.poc_index,
         name="render_poc_dashboard"),
    path("poc_users", views.render_poc_users, name="render_poc_users"),
    path("poc_imp_tweets", views.poc_imp_tweets, name="render_poc_imp_tweets"),

    path("logout", views.logout, name="logout")
]
