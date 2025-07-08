from rest_framework import generics, response, views, exceptions, status
from django.core.exceptions import PermissionDenied as DjangoPermissionDenied


def custom_exception_handler(exc, content):
    response = views.exception_handler(exc, content)
    if response is not None:
        if isinstance(exc, exceptions.NotAuthenticated):
            code = "not_authenticated"
            status_code = status.HTTP_401_UNAUTHORIZED
        elif isinstance(exc, exceptions.AuthenticationFailed):
            code = "authentication_failed"
            status_code = status.HTTP_401_UNAUTHORIZED
        elif isinstance(exc, (exceptions.PermissionDenied, DjangoPermissionDenied)):
            code = "permission_denied"
            status_code = status.HTTP_403_FORBIDDEN
        elif isinstance(exc, exceptions.NotFound):
            code = "not_found"
            status_code = status.HTTP_404_NOT_FOUND
        elif isinstance(exc, exceptions.ValidationError):
            code = "validation_error"
            status_code = status.HTTP_400_BAD_REQUEST
        else:
            code = "unhandled_error"
            status_code = response.status_code
        
        message = response.data.get("details",str(exc))
        response.data = {
            "success": False,
            "error": {
                "code": code,
                "message": message,
            },
        }
        response.status_code = status_code
        return response
# If DRF doesn't handle it, return a generic server error
    return response.Response(
        {
            "success": False,
            "error": {
                "code": "error",
                "message": "An unexpected error occurred.",
            },
        },
        status=status.HTTP_500_INTERNAL_SERVER_ERROR,
    )


class BaseListAPIView(generics.ListAPIView):
    def list(self, request, *args, **kwargs):
        try:
            queryset = self.get_queryset()
            serializer = self.serializer_class(queryset, many=True)
            return response.Response(
                {
                    "success": True,
                    "data": serializer.data
                },
                status=status.HTTP_200_OK,
            )
        except Exception as e:
            return custom_exception_handler(e, {"request": request})

class BaseCreateAPIView(generics.CreateAPIView):
    def create(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data = request.data)
            serializer.is_valid(raise_exception = True)
            self.perform_create(serializer)
            return response.Response(
                {
                    "success": True,
                    "data": serializer.data,
                },
                status=status.HTTP_200_OK,
            )
        except Exception as e:
            return custom_exception_handler(e, {"request": request})

class BaseListCreateView(BaseListAPIView,BaseCreateAPIView):
    pass
