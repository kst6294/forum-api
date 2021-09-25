from rest_framework import permissions


# 작성자 외에는 읽기만 가능한 커스텀 permission 
class IsOwnerOrReadOnly(permissions.BasePermission):

    # 읽기 권한 요청이 들어오면 허용하기
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # 사용자와 작성자가 동일한지 확인
        return obj.user == request.user
