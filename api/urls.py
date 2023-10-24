from rest_framework import routers
from .views import DepartmentViewSet, EmployeeViewSet

app_name = 'api'

router = routers.DefaultRouter(trailing_slash=False)
router.register('departments', DepartmentViewSet, basename='departments')
router.register('employees', EmployeeViewSet, basename='employees')

urlpatterns = router.urls
