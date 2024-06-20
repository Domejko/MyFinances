from django.shortcuts import render

from backend.types.htmx import HtmxHttpRequest
from backend.utils.decorators import team_permission_required


@team_permission_required(redirect_url="dashboard", permission="backend.view_client")
def clients_dashboard_endpoint(request: HtmxHttpRequest):
    return render(request, "pages/clients/dashboard/dashboard.html")
